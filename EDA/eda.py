import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("EDA/students.csv")

print(data.head())
print(data.info())
print(data.describe())
print(data.isnull().sum())

data["Marks"].hist()
plt.title("Student Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.savefig("marks_distribution.png")

print("EDA completed successfully!")
