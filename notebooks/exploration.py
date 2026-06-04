import pandas as pd

# Load dataset
df = pd.read_csv("../data/student_data.csv")

print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nStatistics:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())
