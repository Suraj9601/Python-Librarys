import pandas as pd

df = pd.read_json("Files/students.json")

print(df.info())