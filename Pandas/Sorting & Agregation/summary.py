import pandas as pd

data = {
    "Name" : ["Arun", "Varun", "Karan"],
    "Age" : [25, 31, 9],
    "Salary" : [10000,20000,30000]
}

df = pd.DataFrame(data)


avg_salary = df['Salary'].mean()
min_salary = df['Salary'].min()
max_salary = df['Salary'].max()
print("Min Salary : ",min_salary)
print("Max Salary : ",max_salary)
print("Avarage Salary : ",avg_salary)

