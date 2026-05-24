import requests
import os
import re
from dotenv import load_dotenv
import streamlit as st
load_dotenv()
API_KEY = st.secrets["OPENROUTER_API_KEY"]


# -----------------------------
# Extract Duration
# -----------------------------

def extract_duration(text):

    text = text.lower()

    # Match months
    month_match = re.search(r'(\d+)\s*month', text)

    if month_match:
        return int(month_match.group(1))

    # Match years
    year_match = re.search(r'(\d+)\s*year', text)

    if year_match:
        return int(year_match.group(1)) * 12

    return 3


# -----------------------------
# Generate Course Function
# -----------------------------

def generate_course(user_prompt):

    duration = extract_duration(user_prompt)

    prompt = f"""
Create a personalized learning roadmap.

User Request:
{user_prompt}

IMPORTANT:
Generate EXACTLY {duration} months.

STRICT RULES:
- Every month must be UNIQUE
- No repeated content
- Keep roadmap concise
- Include:
  - Topics
  - 1 Mini Project
  - Resources
  - Practice Platforms
- Include REAL links
- Beginner friendly
- Clean markdown formatting

FORMAT:

## Month 1 - Title

Topics:
- Topic 1
- Topic 2

Project:
- One project

Resources:
- https://example.com

Practice:
- LeetCode / HackerRank

Continue until Month {duration}.
"""

    try:

        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",

            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },

            json={
                "model": "openrouter/auto",

                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            }
        )

        data = response.json()

        print(data)

        if "choices" in data:

            return data["choices"][0]["message"]["content"]

        else:

            return f"API Error: {data}"

    except Exception as e:

        return f"Error: {str(e)}"