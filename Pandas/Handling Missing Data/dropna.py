#dropna()

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
print()

df.dropna(inplace=True) # axis = 0 for row and axis = 1 for column acess particular
print(df)