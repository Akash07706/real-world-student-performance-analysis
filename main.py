"""
Real-World Student Performance Analysis
Dataset: UCI Student Performance - Mathematics (student-mat.csv)
Run: python main.py
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parent
OUT = BASE / "visualizations"
OUT.mkdir(exist_ok=True)

# UCI source CSV is semicolon-separated.
df = pd.read_csv(BASE / "student-mat.csv", sep=";")
print("Dataset shape:", df.shape)
print("\nMissing values:", int(df.isna().sum().sum()))
print("Duplicate rows:", int(df.duplicated().sum()))
print("\nFinal grade summary:\n", df["G3"].describe())
print("\nCorrelation with final grade:\n", df[["studytime", "absences", "G1", "G2", "G3"]].corr()["G3"])

# Validation: retain valid observations; do not fabricate or remove data.
clean = df.copy()
clean.columns = clean.columns.str.strip()
clean.to_csv(BASE / "cleaned_student_performance.csv", index=False)

charts = [
    ("hist", "G3", "Distribution of Final Grades (G3)", "Final grade", "Number of students", "final_grade_distribution.png"),
    ("scatter", "studytime", "Study Time vs Final Grade", "Study time category (1=lowest, 4=highest)", "Final grade (G3)", "studytime_vs_final_grade.png"),
    ("scatter", "absences", "Absences vs Final Grade", "Number of school absences", "Final grade (G3)", "absences_vs_final_grade.png"),
]
for kind, col, title, xlabel, ylabel, filename in charts:
    plt.figure(figsize=(8, 5))
    if kind == "hist":
        plt.hist(df[col], bins=11, edgecolor="black")
    else:
        plt.scatter(df[col], df["G3"], alpha=0.55)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(OUT / filename, dpi=160)
    plt.close()

plt.figure(figsize=(8, 5))
plt.bar(["G1", "G2", "G3"], [df.G1.mean(), df.G2.mean(), df.G3.mean()])
plt.title("Average Grades Across Three Periods")
plt.xlabel("Grade period")
plt.ylabel("Average grade")
plt.tight_layout()
plt.savefig(OUT / "average_grades.png", dpi=160)
plt.close()

print("\nAnalysis complete. Cleaned copy and visualizations saved.")
