import pandas as pd

data = {
    "Name" : ["Arun", "Varun", "Karan"],
    "Age" : [25, 31, 9],
    "Salary" : [10000,20000,30000]
}

df = pd.DataFrame(data)
print(df)

df.sort_values(by=["Age", "Salary"], ascending=[True, False], inplace=True)

print(df)