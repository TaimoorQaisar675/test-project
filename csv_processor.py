import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("dataset/people.csv")

# Print the contents
print(df)

# Plot Salary column (assuming there's a 'Salary' column)
plt.figure(figsize=(10, 6))
plt.plot(df["Name"], df["Salary"], marker='o', linestyle='-', color='green')
plt.title("Salary by Person")
plt.xlabel("Name")
plt.ylabel("Salary")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()