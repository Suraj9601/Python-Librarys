import pandas as pd

data = {
    "Name" : ["Suraj", "Smit", "Ketan", "Omkar", "Ram", "Alok"],
    "Age": [19, 19, 20, 17, 16, 21],
    "City" : ["Solapur", "Yavatmal", "Dhule", "Baramati", "Mumbai", "Pune"]
}
df = pd.DataFrame(data)
print(df)

# df.to_csv("Files/output.csv",index=False)
df.to_excel("Files/output.xlsx", index=False)
df.to_json("Files/output.json", index=False)