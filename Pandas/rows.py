#head() or head(n) top rows
#tail() or tail(n) bottom rows

import pandas as pd

df = pd.read_json("Files/students.json")

print("Top rows : ")
print(df.head())
print("Bottom rows :")
print(df.tail())
