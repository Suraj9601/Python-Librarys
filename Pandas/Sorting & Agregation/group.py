import pandas as pd

data = {
    "Name" : ["Arun", "Varun", "Karan", "Narun", "Marun"],
    "Age" : [25, 31, 9, 25, 28],
    "Salary" : [60000,45000,50000, 48000, 52000]
}

df = pd.DataFrame(data)
# Grouped by same age
grouped= df.groupby(['Age','Salary'])['Salary'].sum()
print(grouped)