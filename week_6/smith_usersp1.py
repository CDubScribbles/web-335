"""
Title: smith_usersp1.py
Author: Cliff Smith
Date: July 25, 2026
Description: This program connects to the web355DB MongoDB database using
pymongo and performs several read operations on the users collection.
"""

# Import the MongoClient so we can connect to our MongoDB database
from pymongo import MongoClient

# Build a connection string to connect to our web355DB database
client = MongoClient("mongodb+srv://web355_admin:s3cret@bellevueuniversity.brnh6kg.mongodb.net/web355DB")

# Configure a variable to access the web355DB database
db = client['web355DB']

# Display all documents in the users collection
print("All users:")
for user in db.users.find():
    print(user)

# Display the document where employeeId is 1011
print("\nUser with employeeId 1011:")
print(db.users.find_one({"employeeId": "1011"}))

# Display the document where lastName is Mozart
print("\nUser with lastName Mozart:")
print(db.users.find_one({"lastName": "Mozart"}))