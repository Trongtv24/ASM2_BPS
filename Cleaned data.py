import pandas as pd

# Read the CSV file
file_path = 'Sale_BPS.csv'  # Ensure the path is correct
data = pd.read_csv(file_path)

# Display the first few rows of data
print("Original data:")
print(data.head())

# Check for missing values
print("\nNumber of missing values in each column:")
print(data.isnull().sum())

# Handle missing data:
# - Fill numeric columns with their mean values
# - Fill string columns with a default value

# Handle missing data:
# Find numeric columns
numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns
# Fill numeric columns with mean values
data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].mean())

# Find string columns
string_cols = data.select_dtypes(include=['object']).columns
# Fill string columns with a default value
data[string_cols] = data[string_cols].fillna('Unknown')

# Check the data again
print("\nData after processing:")
print(data.head())

# Check the number of missing values again
print("\nNumber of missing values after processing in each column:")
print(data.isnull().sum())

# Save the cleaned data to a new CSV file
# Change this path to the desired location on your system
output_file_path = 'Sale_BPS_Cleaned.csv'
data.to_csv(output_file_path, index=False)

print(f"\nData has been successfully saved to {output_file_path}")
