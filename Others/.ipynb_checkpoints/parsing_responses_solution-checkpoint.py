#import libraries
import requests
import pandas as pd

# --- Question 1: GET Request ---
print("GET Request")

# Step 1 & 2: Fetch data and print status code
get_response = requests.get("https://jsonplaceholder.typicode.com/posts")
print(f"Status Code: {get_response.status_code}\n")

# Step 3: Convert JSON response to DataFrame and print head
posts_data = get_response.json()
df = pd.DataFrame(posts_data)

print("First 5 rows of DataFrame:")
print(df.head())

# --- Question 2: HEAD Request ---
print("\n HEAD Request")

# Step 1 & 2: Send HEAD request and print response headers
head_response = requests.head("https://jsonplaceholder.typicode.com/posts")
print(f"\nStatus Code: {head_response.status_code}")

print("\n Response Headers:")
for header, value in head_response.headers.items():
    print(f"{header}: {value}")
