
import streamlit as st
import pandas as pd
from pathlib import Path

# Page Configuration
st.set_page_config(
    page_title="Job Market Intelligence",
    page_icon="📊",
    layout="wide"
)


# Custom Dashboard Styling
st.markdown("""


<style>

.stApp {
    background: linear-gradient(135deg, #10172A, #1B1745, #172554);
    color: #FFFFFF;
}

/* Main headings */
h1 {
    color: #A78BFA !important;
    font-weight: 800 !important;
}

h2 {
    color: #38BDF8 !important;
    font-weight: 700 !important;
}

h3 {
    color: #F0ABFC !important;
    font-weight: 700 !important;
}

/* Normal text */
p, label, li {
    color: #E2E8F0;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #24134D, #172554);
    border-right: 2px solid #6366F1;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #C4B5FD !important;
}

[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] li {
    color: #F8FAFC !important;
}

/* Metric Cards */
[data-testid="stMetric"] {
    background: linear-gradient(135deg, #312E81, #1D4ED8);
    border: 1px solid #818CF8;
    padding: 22px;
    border-radius: 18px;
    box-shadow: 0 5px 20px rgba(99, 102, 241, 0.25);
}

[data-testid="stMetricLabel"] {
    color: #E0E7FF !important;
}

[data-testid="stMetricValue"] {
    color: #67E8F9 !important;
    font-weight: 800;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(90deg, #7C3AED, #2563EB);
    color: white !important;
    border: none;
    border-radius: 12px;
    padding: 12px 22px;
    font-weight: 700;
    transition: 0.3s;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #DB2777, #7C3AED);
    border: none;
    color: white !important;
    transform: translateY(-2px);
}

/* Download Button */
.stDownloadButton > button {
    background: linear-gradient(90deg, #059669, #0D9488);
    color: white !important;
    border: none;
    border-radius: 12px;
    font-weight: bold;
}

/* Select boxes */
[data-baseweb="select"] > div {
    background-color: #25245A;
    border: 1px solid #818CF8;
    border-radius: 10px;
    color: white;
}

/* Dataframe */
[data-testid="stDataFrame"] {
    border: 1px solid #6366F1;
    border-radius: 12px;
}

/* Dividers */
hr {
    border-color: #6366F1;
}

/* Info messages */
[data-testid="stAlert"] {
    border-radius: 12px;
}

/* Caption */
.stCaption {
    color: #CBD5E1 !important;
}

</style>


</style>
""", unsafe_allow_html=True)


# Load Dataset
project_path = Path(__file__).resolve().parent.parent
df = pd.read_csv(project_path / "dataset" / "jobs.csv")

# Dashboard Title
st.title("📊 Job Market Intelligence Dashboard")
st.write("Analyze job market trends, salaries and skill requirements.")

st.divider()

# Sidebar Filters
st.sidebar.header("Dashboard Filters")

# Sidebar Project Information
st.sidebar.title("🚀 Job Intelligence")

st.sidebar.write(
    "An AI & Data Science project for analyzing "
    "job market trends and student skill gaps."
)

st.sidebar.divider()

st.sidebar.subheader("🛠️ Technologies")
st.sidebar.write("• Python")
st.sidebar.write("• Pandas")
st.sidebar.write("• Matplotlib")
st.sidebar.write("• Streamlit")

st.sidebar.divider()

st.sidebar.caption("Developed as a BTech CSE AI & DS project")


locations = ["All"] + sorted(df["location"].dropna().unique().tolist())

selected_location = st.sidebar.selectbox(
    "Select Location",
    locations
)

if selected_location != "All":
    filtered_df = df[df["location"] == selected_location]
else:
    filtered_df = df.copy()

# Key Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Jobs", len(filtered_df))

with col2:
    st.metric(
        "Average Salary",
        f"{filtered_df['salary_lpa'].mean():.2f} LPA"
    )

with col3:
    st.metric(
        "Job Roles",
        filtered_df["job_title"].nunique()
    )

st.divider()

# Job Market Data
st.subheader("Available Job Listings")
st.dataframe(filtered_df, use_container_width=True)

# Salary Analysis
st.subheader("Average Salary by Job Role")

salary_data = filtered_df.groupby("job_title")["salary_lpa"].mean()

st.bar_chart(salary_data)

# Skills Demand Analysis
st.subheader("Most Demanded Skills")

all_skills = []

for skills in filtered_df["skills"].dropna():
    for skill in skills.split(","):
        all_skills.append(skill.strip().title())

skill_counts = pd.Series(all_skills).value_counts()

st.bar_chart(skill_counts)

st.divider()

# Skills Gap Analyzer
st.header("🎯 Student Skills Gap Analyzer")

job_roles = sorted(df["job_title"].unique())

selected_role = st.selectbox(
    "Select Your Target Job Role",
    job_roles
)

role_data = df[
    df["job_title"].str.lower() == selected_role.lower()
    ]

required_skills = set()

for skills in role_data["skills"].dropna():
    for skill in skills.split(","):
        required_skills.add(skill.strip().lower())

all_available_skills = sorted({
    skill.strip().lower()
    for skills in df["skills"].dropna()
    for skill in skills.split(",")
})

student_skills = st.multiselect(
    "Select Your Current Skills",
    all_available_skills
)


if st.button("Analyze My Skills"):

    matched = required_skills.intersection(
        {skill.lower() for skill in student_skills}
    )

    missing = required_skills - matched

    if required_skills:
        percentage = len(matched) / len(required_skills) * 100
    else:
        percentage = 0

    st.subheader("Your Analysis")

    st.metric("Skill Match", f"{percentage:.2f}%")

    st.write("✅ Matched Skills:", ", ".join(sorted(matched)) or "None")

    st.write("❌ Missing Skills:", ", ".join(sorted(missing)) or "None")

    if missing:
        st.info(
            "Recommended Skills to Learn: "
            + ", ".join(sorted(missing))
        )
    else:
        st.success("Great! You have all the required skills.")

    # Generate Downloadable Report
    report_data = []

    for skill in sorted(required_skills):
        report_data.append({
            "Target Job Role": selected_role,
            "Match Percentage": round(percentage, 2),
            "Skill": skill.title(),
            "Status": "Matched" if skill in matched else "Missing"
        })

    report_df = pd.DataFrame(report_data)

    st.download_button(
        label="📥 Download Skills Gap Report",
        data=report_df.to_csv(index=False).encode("utf-8"),
        file_name="skills_gap_report.csv",
        mime="text/csv"
    )

# About Project Section
st.divider()

st.header("ℹ️ About This Project")

st.write("""
Job Market Intelligence & Skills Gap Analyzer is a
Data Science project designed to analyze job market trends.

It helps students understand:
- Available job roles and salary trends.
- Most demanded technical skills.
- Their current skills compared to job requirements.
- Skills they need to learn for their target career.

The project uses Python, Pandas and Streamlit.
""")

st.caption("Project Category: Data Science & Analytics | BTech CSE AI & DS")
