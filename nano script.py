import pandas as pd
import numpy as np

df = pd.read_csv("dirty_data.csv")

print("Original Data:\n", df)

# 3️⃣ Handle missing values
df['Age'].fillna(df['Age'].median(), inplace=True) 
df['Salary'].fillna(df['Salary'].mean(), inplace=True)

df.drop_duplicates(inplace=True)

df['Joining_Date'] = pd.to_datetime(df['Joining_Date'])

df['Department'] = df['Department'].str.lower()

df.to_csv("cleaned_data.csv", index=False)
