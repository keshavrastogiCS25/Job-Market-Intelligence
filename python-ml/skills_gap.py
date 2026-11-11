
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

print("SKILLS GAP ANALYZER")
print("-------------------")

# 1. Load Dataset
project_path = Path(__file__).resolve().parent.parent
df = pd.read_csv(project_path / "dataset" / "jobs.csv")

# 2. Available Job Roles
print("\nAvailable Job Roles:")
print(df["job_title"].unique())

# 3. Ask Student for Target Job Role
target_role = input("\nEnter your target job role: ").strip().title()

print("\nYour Target Role:", target_role)

# 4. Ask Student for Their Skills
student_input = input("\nEnter your skills (comma separated): ")

student_skills = [
    skill.strip().title()
    for skill in student_input.split(",")
    if skill.strip()
]

print("\nYour Skills:", student_skills)

# 5. Find Required Skills for Selected Job Role
df["job_title"] = df["job_title"].astype(str).str.strip()

role_jobs = df[
    df["job_title"].str.casefold() == target_role.casefold()
]

print("\nMatching Job Records:", len(role_jobs))

required_skills = []

for skills in role_jobs["skills"]:
    skill_list = [
        skill.strip().title()
        for skill in skills.split(",")
        if skill.strip()
    ]
    required_skills.extend(skill_list)

required_skills = list(set(required_skills))

print("\nRequired Skills:", required_skills)

# 6. Compare Student Skills with Required Skills
student_skill_set = {skill.casefold() for skill in student_skills}

matched_skill_list = [
    skill for skill in required_skills
    if skill.casefold() in student_skill_set
]

missing_skills = [
    skill for skill in required_skills
    if skill.casefold() not in student_skill_set
]

print("\nSkills You Already Have:")
print(matched_skill_list)

print("\nMissing Skills:")
print(missing_skills)

# 7. Calculate Skills Match Percentage
total_skills = len(required_skills)
matched_skills = len(matched_skill_list)

if total_skills > 0:
    match_percentage = (matched_skills / total_skills) * 100
else:
    match_percentage = 0

print("\n----- SKILLS GAP REPORT -----")
print("Total Required Skills:", total_skills)
print("Skills Matched:", matched_skills)
print("Skills Missing:", len(missing_skills))
print("Skills Match Percentage:", round(match_percentage, 2), "%")

# 8. Visualize Skills Gap
labels = ["Matched Skills", "Missing Skills"]
values = [matched_skills, len(missing_skills)]

plt.figure(figsize=(7, 5))

bars = plt.bar(labels, values)

plt.title("Student Skills Gap Analysis")
plt.xlabel("Skill Category")
plt.ylabel("Number of Skills")

plt.bar_label(bars)
plt.ylim(0, max(values) + 1 if max(values) > 0 else 1)

plt.tight_layout()
plt.show()

# 9. Skill Recommendations
print("\n----- SKILL RECOMMENDATIONS -----")

recommendations = {
    "Python": "Python Official Documentation",
    "Sql": "W3Schools SQL Tutorial",
    "Machine Learning": "Scikit-learn Tutorials",
    "Excel": "Microsoft Excel Learning",
    "Power Bi": "Microsoft Power BI Learning",
    "Java": "Oracle Java Tutorials",
    "Spring Boot": "Spring Boot Official Guides",
    "Tensorflow": "TensorFlow Tutorials",
    "Django": "Django Official Documentation"
}

if missing_skills:
    print("Recommended Learning Resources:\n")

    for skill in missing_skills:
        resource = recommendations.get(
            skill,
            "Search for beginner tutorials online"
        )

        print("Missing Skill:", skill)
        print("Recommended Resource:", resource)
        print("---------------------------")

else:
    print("Great! You have all the required skills.")

# 10. Invalid Job Role Check
if role_jobs.empty:
    print("\nNote: This job role is not available in our demo dataset.")
    print("Please select a role from the available job roles.")

# 11. Generate CSV Report

# 11. Generate Improved CSV Report

report_data = []

for skill in required_skills:
    if skill.casefold() in student_skill_set:
        status = "Matched"
    else:
        status = "Missing"

    report_data.append({
        "Target Job Role": target_role,
        "Match Percentage": str(round(match_percentage, 2)) + "%",
        "Skill": skill,
        "Status": status
    })

report_df = pd.DataFrame(report_data)

report_path = project_path / "skills_gap_report.csv"

report_df.to_csv(report_path, index=False)

print("\n----- IMPROVED CSV REPORT GENERATED -----")
print("Report saved successfully!")
print("File Location:", report_path)

# 12. Skill Priority System

print("\n----- SKILL PRIORITY SYSTEM -----")

skill_priority = {
    "Python": "High",
    "Sql": "High",
    "Machine Learning": "High",
    "Power Bi": "Medium",
    "Excel": "Medium",
    "Django": "Medium",
    "Spring Boot": "Medium",
    "Tensorflow": "High",
    "Java": "High"
}

for skill in missing_skills:

    priority = skill_priority.get(
        skill,
        "Low"
    )

    print("Missing Skill:", skill)
    print("Priority:", priority)
    print("---------------------------")