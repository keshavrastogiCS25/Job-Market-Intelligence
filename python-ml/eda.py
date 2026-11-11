
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# 1. Load Dataset
print("JOB MARKET INTELLIGENCE PROJECT")
print("--------------------------------")

df = pd.read_csv("../dataset/jobs.csv")

print("\nComplete Dataset:")
print(df.to_string())

# 2. Dataset Shape
print("\nDataset Shape:")
print(df.shape)

# 3. Dataset Information
print("\nDataset Information:")
df.info()

# 4. Statistical Summary
print("\nStatistical Summary:")
print(df.describe())

# 5. Job Role Distribution
print("\nJob Role Distribution:")
print(df["job_title"].value_counts())

# 6. Average Salary Analysis
print("\nAverage Salary by Job Role:")

salary_analysis = df.groupby("job_title")["salary_lpa"].mean()

print(salary_analysis)

# 7. Salary Bar Graph
plt.figure(figsize=(10, 5))

plt.bar(salary_analysis.index, salary_analysis.values)

plt.title("Average Salary by Job Role")
plt.xlabel("Job Role")
plt.ylabel("Salary (LPA)")
plt.xticks(rotation=45)

plt.tight_layout()

# 8. Skills Demand Analysis
all_skills = []

for skills in df["skills"]:
    skill_list = [skill.strip() for skill in skills.split(",")]
    all_skills.extend(skill_list)

skill_counts = Counter(all_skills)

print("\nSkills Demand Analysis:")
for skill, count in skill_counts.most_common():
    print(skill, ":", count)

# 9. Skills Demand Graph

plt.figure(figsize=(10, 5))

plt.bar(skill_counts.keys(), skill_counts.values())

plt.title("Most Demanded Skills")
plt.xlabel("Skills")
plt.ylabel("Number of Job Postings")
plt.xticks(rotation=45)

plt.tight_layout()

# 10. Display Graphs
plt.show()
