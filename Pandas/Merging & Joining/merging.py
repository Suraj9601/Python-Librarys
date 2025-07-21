# pd.merge(df1, df2, on="column_name", how="type of join")

import pandas as pd

df_costemer = pd.DataFrame({
    "CustomerID": [1,2,3],
    "Name": ['Ramesh', 'Suresh', 'Kalpesh']
})

df_orders = pd.DataFrame({
    "CustomerID": [1,2,4],
    "OrderAmount": [250, 450, 350]
})

df_merged = pd.merge(df_costemer, df_orders, on="CustomerID", how="right")
print(df_merged)