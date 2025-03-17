import pandas as pd
import os
print(os.getcwd())

print(2+2)
file_path='../csv/credits.csv'
df = pd.read_csv(file_path)
print(df.head())




