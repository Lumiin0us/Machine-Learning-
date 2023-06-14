import pandas as pd
from sklearn.preprocessing import OneHotEncoder

#Importing dataset
df = pd.read_csv("DataPreprocessing/Data.csv")

#separating dependent and independent columns
df_x = df.iloc[:, [0, 1, 2]]
df_y = df.iloc[:, -1]

print(df_y.head())