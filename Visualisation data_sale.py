import pandas as pd
import matplotlib.pyplot as plt

# Read the data from a CSV file
df = pd.read_csv('DataSale_BPS.csv')

# Convert SaleDate to datetime
df['SaleDate'] = pd.to_datetime(df['SaleDate'])

# Plot 1: Total Sales by Month
df['Month'] = df['SaleDate'].dt.to_period('M')
sales_by_month = df.groupby('Month')['TotalPrice'].sum()

plt.figure(figsize=(10, 5))
sales_by_month.plot(kind='bar')
plt.title('Total Sales by Month')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()

# Plot 2: Sales by Payment Method
sales_by_payment = df.groupby('PaymentMethod')['TotalPrice'].sum()

plt.figure(figsize=(10, 5))
sales_by_payment.plot(kind='bar', color='skyblue')
plt.title('Sales by Payment Method')
plt.xlabel('Payment Method')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()

# Plot 3: Sales by Sales Channel
sales_by_channel = df.groupby('SalesChannel')['TotalPrice'].sum()

plt.figure(figsize=(10, 5))
sales_by_channel.plot(kind='bar', color='green')
plt.title('Sales by Sales Channel')
plt.xlabel('Sales Channel')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()
