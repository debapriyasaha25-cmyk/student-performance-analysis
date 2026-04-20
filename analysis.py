import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("student-por.csv")

# Check columns
print("Columns:\n", df.columns)

# ---------------- PROCESSING ----------------

# Use correct columns (G1, G2, G3)
df["Total"] = df["G1"] + df["G2"] + df["G3"]
df["Average"] = df["Total"] / 3

print(df.head())

# ---------------- ANALYSIS ----------------

# Top students
top_students = df.sort_values(by="Average", ascending=False).head(5)
print("\nTop Students:\n", top_students)

# Gender-wise performance
print("\nAverage by Gender:\n", df.groupby("sex")["Average"].mean())

# Study time impact
print("\nStudy Time Impact:\n", df.groupby("studytime")["Average"].mean())

# ---------------- VISUALIZATION ----------------

# Average distribution
sns.histplot(df["Average"], bins=10, kde=True)
plt.title("Average Marks Distribution")
plt.show()

# Gender vs performance
sns.barplot(x="sex", y="Average", data=df)
plt.title("Gender vs Average Marks")
plt.show()

# Study time vs performance
sns.barplot(x="studytime", y="Average", data=df)
plt.title("Study Time vs Performance")
plt.show()