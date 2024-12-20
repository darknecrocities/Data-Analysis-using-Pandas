import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv('data.csv')

# Display the first few rows of the dataset
print("First 5 rows of the dataset:")
print(data.head())

# Basic statistics
print("\nBasic Statistics:")
print(data.describe())

# Data types of each column
print("\nData Types of Each Column:")
print(data.dtypes)

# Check for missing values
print("\nMissing Values in Each Column:")
print(data.isnull().sum())

# Select only numeric columns for correlation matrix
numeric_data = data.select_dtypes(include=[float, int])

# Correlation matrix
print("\nCorrelation Matrix:")
print(numeric_data.corr())

# Group by a specific column (e.g., 'Category') and calculate the mean for numeric columns
if 'Category' in data.columns:
    print("\nMean values grouped by 'Category':")
    numeric_columns = numeric_data.columns
    grouped_data = data.groupby('Category')[numeric_columns].mean()
    print(grouped_data)

# Plotting (optional, requires matplotlib)
# Histogram of a specific column (e.g., 'Value')
if 'Value' in data.columns:
    plt.hist(data['Value'], bins=20)
    plt.title('Histogram of Value')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()

# Save the processed data to a new CSV file
data.to_csv('processed_data.csv', index=False)

print("\nProcessed data saved to 'processed_data.csv'")