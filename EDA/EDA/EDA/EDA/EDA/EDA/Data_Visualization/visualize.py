import pandas as pd
import matplotlib.pyplot as plt
import os

data = pd.read_csv("Student.csv")

plt.figure(figsize=(8, 5))
plt.bar(data["Name"], data["Marks"])

plt.title("Student Marks Comparison")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.xticks(rotation=45)

os.makedirs("Data_Visualization/outputs", exist_ok=True)
plt.tight_layout()
plt.savefig("Data_Visualization/outputs/marks_chart.png")

print("Chart created successfully!")
