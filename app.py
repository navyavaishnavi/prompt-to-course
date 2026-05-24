import streamlit as st
from fpdf import FPDF
from generator import generate_course

# -----------------------------
# PDF Generator
# -----------------------------

def create_pdf(content):

    pdf = FPDF()

    pdf.set_auto_page_break(
        auto=True,
        margin=15
    )

    pdf.add_page()

    pdf.set_font(
        "Arial",
        size=12
    )

    # Clean unsupported unicode

    clean_content = content.encode(
        "latin-1",
        "ignore"
    ).decode(
        "latin-1"
    )

    clean_content = clean_content.replace("#", "")
    clean_content = clean_content.replace("*", "")
    clean_content = clean_content.replace("`", "")

    lines = clean_content.split("\n")

    for line in lines:

        if not line.strip():

            pdf.ln(4)

            continue

        if len(line) > 300:

            line = line[:300]

        try:

            pdf.multi_cell(
                180,
                8,
                line
            )

        except:

            continue

    pdf_file = "roadmap.pdf"

    pdf.output(pdf_file)

    return pdf_file


# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="AI Roadmap Generator",
    page_icon="🚀",
    layout="wide"
)

# -----------------------------
# SIDEBAR
# -----------------------------

st.sidebar.title("📊 Dashboard")

st.sidebar.info(
    """
AI Learning Platform

Features:
• AI Roadmaps
• PDF Export
• Progress Tracker
• Resource Links
• Practice Platforms
"""
)

# -----------------------------
# PROFESSIONAL CSS
# -----------------------------

st.markdown("""
<style>

/* -----------------------------
MAIN BACKGROUND
----------------------------- */

.stApp {

    background:
        radial-gradient(
            circle at top right,
            rgba(59,130,246,0.08),
            transparent 20%
        ),

        radial-gradient(
            circle at bottom left,
            rgba(168,85,247,0.06),
            transparent 20%
        ),

        linear-gradient(
            180deg,
            #F8FAFC,
            #EEF2FF
        );

    color: #0F172A;

    background-attachment: fixed;
}

/* -----------------------------
MAIN
----------------------------- */

.main {

    padding-top: 2rem;
}

/* -----------------------------
HERO TITLE
----------------------------- */

.hero-title {

    font-size: 4rem;

    font-weight: 900;

    text-align: center;

    color: #0F172A;

    margin-bottom: 0.5rem;

    letter-spacing: -2px;
}

/* -----------------------------
SUBTITLE
----------------------------- */

.hero-subtitle {

    text-align: center;

    color: #475569;

    margin-bottom: 3rem;

    font-size: 1.2rem;
}

/* -----------------------------
SIDEBAR
----------------------------- */

section[data-testid="stSidebar"] {

    background: rgba(
        255,
        255,
        255,
        0.7
    );

    backdrop-filter: blur(16px);

    border-right: 1px solid rgba(
        0,
        0,
        0,
        0.05
    );
}

/* -----------------------------
LABELS
----------------------------- */

label {

    color: #0F172A !important;

    font-weight: 600 !important;
}

/* -----------------------------
TEXT AREA
----------------------------- */

.stTextArea textarea {

    background-color: rgba(
        255,
        255,
        255,
        0.8
    ) !important;

    color: #0F172A !important;

    border-radius: 18px !important;

    border: 1px solid rgba(
        0,
        0,
        0,
        0.08
    ) !important;

    font-size: 1rem !important;

    backdrop-filter: blur(12px);
}

/* Placeholder */

.stTextArea textarea::placeholder {

    color: #64748B !important;
}

/* -----------------------------
SELECTBOX
----------------------------- */

.stSelectbox div[data-baseweb="select"] {

    background: rgba(
        255,
        255,
        255,
        0.8
    ) !important;

    border: 1px solid rgba(
        0,
        0,
        0,
        0.08
    ) !important;

    border-radius: 16px !important;

    min-height: 50px !important;

    box-shadow: none !important;
}

/* Internal Select */

.stSelectbox div[data-baseweb="select"] > div {

    background: transparent !important;

    color: #0F172A !important;
}

/* Remove White Inner Box */

.stSelectbox input {

    background: transparent !important;

    color: #0F172A !important;

    caret-color: #0F172A !important;
}

/* Dropdown */

div[data-baseweb="popover"] {

    background-color: white !important;

    border-radius: 12px !important;

    border: 1px solid #E2E8F0 !important;
}

/* Dropdown Options */

li {

    background-color: white !important;

    color: #0F172A !important;
}

/* Hover */

li:hover {

    background-color: #EEF2FF !important;

    color: #2563EB !important;
}

/* -----------------------------
BUTTON
----------------------------- */

.stButton>button {

    width: 100%;

    height: 3.3rem;

    border-radius: 16px;

    border: none;

    font-size: 1rem;

    font-weight: 700;

    color: white;

    background: linear-gradient(
        90deg,
        #2563EB,
        #7C3AED
    );

    transition: 0.3s;

    box-shadow:
        0 8px 25px rgba(
            37,
            99,
            235,
            0.2
        );
}

/* Hover */

.stButton>button:hover {

    transform: translateY(-2px);
}

/* -----------------------------
ROADMAP BOX
----------------------------- */

.roadmap-box {

    padding: 2.5rem;

    border-radius: 24px;

    background: rgba(
        255,
        255,
        255,
        0.75
    );

    backdrop-filter: blur(18px);

    border: 1px solid rgba(
        255,
        255,
        255,
        0.6
    );

    margin-top: 2rem;

    box-shadow:
        0 10px 40px rgba(
            15,
            23,
            42,
            0.08
        );
}

/* -----------------------------
METRICS
----------------------------- */

[data-testid="metric-container"] {

    background-color: rgba(
        255,
        255,
        255,
        0.8
    );

    border: 1px solid rgba(
        0,
        0,
        0,
        0.06
    );

    padding: 1rem;

    border-radius: 18px;
}

/* -----------------------------
TEXT
----------------------------- */

p, span, div {

    color: #0F172A;
}

/* -----------------------------
SCROLLBAR
----------------------------- */

::-webkit-scrollbar {

    width: 8px;
}

::-webkit-scrollbar-thumb {

    background: #CBD5E1;

    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# HERO SECTION
# -----------------------------

st.markdown(
    '<div class="hero-title">🚀 AI Learning Roadmap Generator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-subtitle">'
    'Generate AI-powered personalized learning roadmaps instantly.'
    '</div>',
    unsafe_allow_html=True
)

# -----------------------------
# USER INPUT
# -----------------------------

prompt = st.text_area(
    "What do you want to learn?",
    placeholder="Example: Learn Python in 6 months",
    height=150
)

# -----------------------------
# INPUTS
# -----------------------------

col1, col2 = st.columns(2)

with col1:

    level = st.selectbox(
        "Select Your Level",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

with col2:

    goal_type = st.selectbox(
        "Goal Type",
        [
            "Job Ready",
            "Interview Preparation",
            "Competitive Programming",
            "Academic Learning",
            "Project Building"
        ]
    )

hours = st.slider(
    "Study Hours Per Day",
    1,
    10,
    2
)

# -----------------------------
# BUTTON
# -----------------------------

generate = st.button(
    "Generate Roadmap"
)

# -----------------------------
# ROADMAP
# -----------------------------

if generate:

    if prompt.strip() == "":

        st.warning(
            "Please enter a learning goal."
        )

    else:

        full_prompt = f"""
Goal: {prompt}

Level: {level}

Study Hours Per Day: {hours}

Goal Type: {goal_type}

Generate roadmap according to user's duration.

Rules:
- Keep concise
- Unique months
- No repetition
- Include:
  - Topics
  - Mini project
  - Resources
  - Practice websites
- Use REAL resource links
- Beginner friendly
- Clean markdown
"""

        with st.spinner(
            "Generating your AI roadmap..."
        ):

            roadmap = generate_course(
                full_prompt
            )

            st.markdown(
                '<div class="roadmap-box">',
                unsafe_allow_html=True
            )

            # Metrics

            m1, m2, m3 = st.columns(3)

            m1.metric(
                "Level",
                level
            )

            m2.metric(
                "Hours/Day",
                hours
            )

            m3.metric(
                "Goal",
                goal_type
            )

            st.divider()

            # Roadmap

            st.markdown(
                roadmap
            )

            st.divider()

            # Progress Tracker

            st.subheader(
                "📈 Progress Tracker"
            )

            for i in range(1, 13):

                st.checkbox(
                    f"Complete Month {i}"
                )

            st.markdown(
                '</div>',
                unsafe_allow_html=True
            )

            st.success(
                "✅ Roadmap generated successfully!"
            )

            # PDF Download

            try:

                pdf_file = create_pdf(
                    roadmap
                )

                with open(
                    pdf_file,
                    "rb"
                ) as file:

                    st.download_button(
                        label="📥 Download Roadmap as PDF",
                        data=file,
                        file_name="AI_Roadmap.pdf",
                        mime="application/pdf"
                    )

            except:

                st.warning(
                    "PDF generation temporarily unavailable."
                )