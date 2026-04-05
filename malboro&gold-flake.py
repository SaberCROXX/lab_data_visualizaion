import pandas as pd
import matplotlib.pyplot as plt
file_path = "C:/Users/anjis/Downloads/Cigarette_Sales_India_2024_2025.xlsx"

try:
    df = pd.read_excel(file_path)
    print("File loaded successfully ✅")
except Exception as e:
    print("Error loading file ❌:", e)
df["Label"] = df["Month"] + " " + df["Year"].astype(str)
# 1. LINE GRAPH

plt.figure()
plt.plot(df["Label"], df["Gold Flake (Bn sticks)"], marker='o', label="Gold Flake")
plt.plot(df["Label"], df["Marlboro (Bn sticks)"], marker='o', label="Marlboro")
plt.xticks(rotation=90)
plt.title("Monthly Cigarette Sales - Line Graph")
plt.xlabel("Month-Year")
plt.ylabel("Sales (Bn sticks)")
plt.legend()
plt.tight_layout()
plt.show()
# 2. BAR CHART

plt.figure()
x = range(len(df))
plt.bar(x, df["Gold Flake (Bn sticks)"], label="Gold Flake")
plt.bar(x, df["Marlboro (Bn sticks)"], bottom=df["Gold Flake (Bn sticks)"], label="Marlboro")
plt.xticks(x, df["Label"], rotation=90)
plt.title("Monthly Cigarette Sales - Bar Chart")
plt.xlabel("Month-Year")
plt.ylabel("Sales (Bn sticks)")
plt.legend()
plt.tight_layout()
plt.show()
# 3. PIE CHART

total_gf = df["Gold Flake (Bn sticks)"].sum()
total_mb = df["Marlboro (Bn sticks)"].sum()

plt.figure()
plt.pie([total_gf, total_mb], labels=["Gold Flake", "Marlboro"], autopct='%1.1f%%')
plt.title("Market Share Distribution")
plt.show()
# 4. SCATTER PLOT

plt.figure()
plt.scatter(df["Gold Flake (Bn sticks)"], df["Marlboro (Bn sticks)"])
plt.title("Gold Flake vs Marlboro Sales")
plt.xlabel("Gold Flake (Bn sticks)")
plt.ylabel("Marlboro (Bn sticks)")
plt.show()
# 5. BOX PLOT

plt.figure()
plt.boxplot([df["Gold Flake (Bn sticks)"], df["Marlboro (Bn sticks)"]])
plt.xticks([1, 2], ["Gold Flake", "Marlboro"])
plt.title("Sales Distribution - Box Plot")
plt.ylabel("Sales (Bn sticks)")
plt.show()