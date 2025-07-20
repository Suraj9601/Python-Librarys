#fillna()
#fillna(value, inplace=True)

import pandas as pd

employees = {
    "Name": [None, "Priya Mehta", "Rohit Verma", "Sneha Gupta", "Ravi Singh"],
    "Age": [None, 32, 30, 26, 35],
    "Gender": [None, "Female", "Male", "Female", "Male"],
    "Department": [None, "HR", "Sales", "Marketing", "Finance"],
    "Salary": [None, 60000, 52000, 48000, 70000],
}

df = pd.DataFrame(employees)
print(df)

df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)

# df.fillna(0,inplace=True)
print(df)