import pandas as pd

# Step 1: Read the CSV File
file_path = 'Sale_BPS.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the original data
print("Original Data:")
print(data.head())

# Step 2: Check for Missing Data
print("\nMissing Data Summary:")
print(data.isnull().sum())

# Step 3: Remove Rows with Missing Data
# Drop any rows that contain null values
data_cleaned = data.dropna()

# Check if missing data is handled
print("\nMissing Data After Cleaning:")
print(data_cleaned.isnull().sum())

# Display the first few rows of the cleaned data
print("\nCleaned Data:")
print(data_cleaned.head())

# Step 4: Save the Cleaned Data to a New CSV File
cleaned_file_path = 'Sale_cleaned_BPS.csv'
data_cleaned.to_csv(cleaned_file_path, index=False)

print(f"\nData has been cleaned and saved to '{cleaned_file_path}'")
