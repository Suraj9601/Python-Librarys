import pandas as pd

employees = {
    "Name": ["Anil Kumar", "Priya Mehta", "Rohit Verma", "Sneha Gupta", "Ravi Singh"],
    "Age": [28, 32, 30, 26, 35],
    "Gender": ["Male", "Female", "Male", "Female", "Male"],
    "Department": ["IT", "HR", "Sales", "Marketing", "Finance"],
    "Salary": [55000, 60000, 52000, 48000, 70000],
}

df = pd.DataFrame(employees)

#single condition
high_salary = df[df['Salary']>50000]
# print(high_salary)

#Multiple Condition
filter = df[(df['Salary']>50000) & (df['Age']>30)]
print(filter)
print()
print("OR Condition")
filter_or = df[(df['Salary']>50000) | (df['Age']>30)]
print(filter_or)