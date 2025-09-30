# Step 1: Import required libraries
import sqlite3
import pandas as pd

# Step 2: Connect to the Chinook database
connection = sqlite3.connect("chinook.db")

# Step 3: Define SQL query
query = """
SELECT *
FROM customers
WHERE Country = 'Germany'
"""

# Step 4: Load data using pd.read_sql
df = pd.read_sql(query, connection)

# Step 5: Display the first 5 rows
print(df.head())

# Close the database connection
connection.close()
