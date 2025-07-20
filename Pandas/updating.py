import pandas as pd 

employees = {
    "Name": ["Anil Kumar", "Priya Mehta", "Rohit Verma", "Sneha Gupta", "Ravi Singh"],
    "Age": [28, 32, 30, 26, 35],
    "Gender": ["Male", "Female", "Male", "Female", "Male"],
    "Department": ["IT", "HR", "Sales", "Marketing", "Finance"],
    "Salary": [55000, 60000, 52000, 48000, 70000],
}

df = pd.DataFrame(employees)
print(df)

# Incresing Salary by 5%
df['Salary'] = df["Salary"] * 1.05

print(df)