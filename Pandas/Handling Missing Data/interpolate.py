import pandas as pd 

employees = {
    "Name": ["Anil Kumar", "Priya Mehta", "Rohit Verma", "Sneha Gupta", "Ravi Singh"],
    "Age": [None, 32, 30, 26, 35],
    "Gender": [None, "Female", "Male", "Female", "Male"],
    "Department": [None, "HR", "Sales", "Marketing", "Finance"],
    "Salary": [None, 60000, 52000, 48000, 70000],
}

df = pd.DataFrame(employees)

print("Before interpolation:\n")
print(df)
print()

# Only interpolate numeric columns (Age and Salary)
df[["Age", "Salary"]] = df[["Age", "Salary"]].interpolate(method="linear")

print("After interpolation:\n")
print(df)
