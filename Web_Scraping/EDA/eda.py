Python
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("students.csv")

print("First 5 Records:")
print(data.head())

print("\nDataset Information:")
print(data.info())

print("\nStatistical Summary:")
print(data.describe())

print("\nMissing Values:")
print(data.isnull().sum())

data["Marks"].hist()
plt.title("Student Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.savefig("marks_distribution.png")

print("EDA completed successfully!")
