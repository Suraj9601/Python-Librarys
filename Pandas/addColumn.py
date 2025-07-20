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

#Method 1
df["Bunus"] = df['Salary'] * 0.1 # 10%
print(df)

#Method 2 Insert method presice location
# df.insert(loc, "column_name", some_data)

df.insert(0, "Employee ID", [1,2,3,4,5])
print(df)