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

    # Remove unsupported unicode

    clean_content = content.encode(
        "latin-1",
        "ignore"
    ).decode(
        "latin-1"
    )

    # Remove markdown symbols

    clean_content = clean_content.replace("#", "")
    clean_content = clean_content.replace("*", "")
    clean_content = clean_content.replace("`", "")

    lines = clean_content.split("\n")

    for line in lines:

        # Empty line spacing

        if not line.strip():

            pdf.ln(4)

            continue

        # Prevent long lines crash

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
🚀 AI Learning Platform

Features:
- AI Roadmaps
- PDF Export
- Progress Tracker
- Resource Links
- Practice Platforms
"""
)

# -----------------------------
# MODERN AI CSS
# -----------------------------

st.markdown("""
<style>

/* -----------------------------
MAIN APP BACKGROUND
----------------------------- */

.stApp {

    background:
        radial-gradient(
            circle at top left,
            rgba(37, 99, 235, 0.25),
            transparent 25%
        ),

        radial-gradient(
            circle at bottom right,
            rgba(124, 58, 237, 0.25),
            transparent 25%
        ),

        linear-gradient(
            135deg,
            #020617,
            #0F172A,
            #111827
        );

    color: white;

    background-attachment: fixed;
}

/* Floating Glow */

.stApp::before {

    content: "";

    position: fixed;

    width: 500px;
    height: 500px;

    background: rgba(
        59,
        130,
        246,
        0.15
    );

    filter: blur(120px);

    top: -100px;
    left: -100px;

    z-index: -1;
}

.stApp::after {

    content: "";

    position: fixed;

    width: 500px;
    height: 500px;

    background: rgba(
        168,
        85,
        247,
        0.12
    );

    filter: blur(120px);

    bottom: -100px;
    right: -100px;

    z-index: -1;
}

/* -----------------------------
MAIN
----------------------------- */

.main {

    padding-top: 2rem;
}

/* -----------------------------
HERO SECTION
----------------------------- */

.hero-title {

    font-size: 4rem;

    font-weight: 800;

    text-align: center;

    color: white;

    margin-bottom: 0.5rem;

    letter-spacing: -1px;
}

.hero-subtitle {

    text-align: center;

    color: #CBD5E1;

    margin-bottom: 3rem;

    font-size: 1.2rem;
}

/* -----------------------------
SIDEBAR
----------------------------- */

section[data-testid="stSidebar"] {

    background-color: rgba(
        15,
        23,
        42,
        0.85
    );

    backdrop-filter: blur(12px);

    border-right: 1px solid rgba(
        255,
        255,
        255,
        0.08
    );
}

/* -----------------------------
LABELS
----------------------------- */

label {

    color: white !important;

    font-weight: 600 !important;
}

/* -----------------------------
TEXT AREA
----------------------------- */

.stTextArea textarea {

    background-color: rgba(
        17,
        24,
        39,
        0.8
    ) !important;

    color: white !important;

    border-radius: 18px !important;

    border: 1px solid rgba(
        255,
        255,
        255,
        0.08
    ) !important;

    font-size: 1rem !important;

    backdrop-filter: blur(12px);
}

/* Placeholder */

.stTextArea textarea::placeholder {

    color: #9CA3AF !important;
}

/* -----------------------------
SELECTBOX
----------------------------- */

.stSelectbox div[data-baseweb="select"] {

    background: rgba(
        17,
        24,
        39,
        0.85
    ) !important;

    border: 1px solid rgba(
        255,
        255,
        255,
        0.08
    ) !important;

    border-radius: 16px !important;

    min-height: 50px !important;

    box-shadow: none !important;
}

/* Internal Container */

.stSelectbox div[data-baseweb="select"] > div {

    background: transparent !important;

    color: white !important;
}

/* Remove White Input */

.stSelectbox input {

    background: transparent !important;

    color: white !important;

    caret-color: white !important;
}

/* Dropdown Popup */

div[data-baseweb="popover"] {

    background-color: #111827 !important;

    border-radius: 12px !important;

    border: 1px solid #374151 !important;
}

/* Dropdown Options */

li {

    background-color: #111827 !important;

    color: white !important;
}

/* Hover */

li:hover {

    background-color: #2563EB !important;

    color: white !important;
}

/* -----------------------------
BUTTONS
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

    box-shadow: 0px 0px 20px rgba(
        124,
        58,
        237,
        0.35
    );
}

/* Hover */

.stButton>button:hover {

    transform: translateY(-2px);

    box-shadow: 0px 0px 30px rgba(
        124,
        58,
        237,
        0.55
    );
}

/* -----------------------------
ROADMAP BOX
----------------------------- */

.roadmap-box {

    padding: 2rem;

    border-radius: 24px;

    background: rgba(
        17,
        24,
        39,
        0.65
    );

    backdrop-filter: blur(16px);

    border: 1px solid rgba(
        255,
        255,
        255,
        0.08
    );

    margin-top: 2rem;

    box-shadow: 0px 0px 40px rgba(
        0,
        0,
        0,
        0.35
    );
}

/* -----------------------------
METRICS
----------------------------- */

[data-testid="metric-container"] {

    background-color: rgba(
        17,
        24,
        39,
        0.75
    );

    border: 1px solid rgba(
        255,
        255,
        255,
        0.08
    );

    padding: 1rem;

    border-radius: 18px;
}

/* -----------------------------
GENERAL TEXT
----------------------------- */

p, span, div {

    color: white;
}

/* -----------------------------
SCROLLBAR
----------------------------- */

::-webkit-scrollbar {

    width: 8px;
}

::-webkit-scrollbar-thumb {

    background: #374151;

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
# EXTRA INPUTS
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

            # Roadmap Output

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

            # -----------------------------
            # PDF DOWNLOAD
            # -----------------------------

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
                    "PDF generation temporarily unavailable for this roadmap."
                )