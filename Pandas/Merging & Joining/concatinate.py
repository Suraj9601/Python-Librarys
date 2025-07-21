# Vertically (row-wise)  axis = 0
# Horizontaly (column-wise)  axis = 1

import pandas as pd

df_region1 = pd.DataFrame({
    "CustomerID": [1,2],
    "Name": ['Gopal', 'Raju']
})

df_region2 = pd.DataFrame({
    "CustomerID": [3,4],
    "Name": ['Shyam', 'Abhay']
})

df_concate = pd.concat([df_region1, df_region2], ignore_index=True)
print(df_concate)