#import libraries
import pandas as pd

# Step 1: Read the files
df1 = pd.read_excel("customers_part1.xlsx")
df2 = pd.read_excel("customers_part2.xlsx")
purchases = pd.read_excel("purchases.xlsx")

# Step 2: Append the customer data
customers = pd.concat([df1, df2])

# Step 3: Merge with purchases data
merged_data = pd.merge(customers, purchases, on="CustomerID", how="left")

# Step 4: View results
print(merged_data)
