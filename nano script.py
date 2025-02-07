import pandas as pd
import numpy as np

# 1️⃣ Load the dataset
df = pd.read_csv("dirty_data.csv")

# 2️⃣ Display first few rows before cleaning
print("Original Data:\n", df)

# 3️⃣ Handle missing values
df['Age'].fillna(df['Age'].median(), inplace=True)  # Replace missing Age with median
df['Salary'].fillna(df['Salary'].mean(), inplace=True)  # Replace missing Salary with mean

# 4️⃣ Remove duplicate rows
df.drop_duplicates(inplace=True)

# 5️⃣ Convert Joining_Date column to datetime format
df['Joining_Date'] = pd.to_datetime(df['Joining_Date'])

# 6️⃣ Convert Department names to lowercase for consistency
df['Department'] = df['Department'].str.lower()

# 7️⃣ Save the cleaned data to a new CSV file
df.to_csv("cleaned_data.csv", index=False)
