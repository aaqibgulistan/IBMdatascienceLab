import pandas as pd

# Load the CSV file
df = pd.read_csv("data.csv")

# Process the data
df = df.dropna() # Drop rows with missing values
df = df.groupby("column_name").sum() # Group by a column and sum

# Print the processed data
print(df)