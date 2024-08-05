import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the data from the uploaded file
file_path = 'DataSale_BPS.csv'
data = pd.read_csv(file_path)

# Select the features and target variable
X = data[['Quantity', 'UnitPrice']]
y = data['TotalPrice']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create the linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Plotting the line chart for the prediction
plt.figure(figsize=(10, 6))
plt.plot(y_test.values, label='Actual TotalPrice')
plt.plot(y_pred, label='Predicted TotalPrice', linestyle='--')
plt.xlabel('Sample Index')
plt.ylabel('TotalPrice')
plt.title('Line Chart of Actual vs Predicted TotalPrice')
plt.legend()
plt.show()
