import pandas as pd

# Load dataset
df = pd.read_excel("customer_orders.xlsx")

# Shape before cleaning
print("Shape before cleaning:", df.shape)

print("\nMissing values per column:")
print(df.isna().sum())

for col in df.select_dtypes(include="number").columns:
    df[col] = df[col].fillna(df[col].median())

# Remove duplicate rows
df = df.drop_duplicates()


print("\nShape after cleaning:", df.shape)
