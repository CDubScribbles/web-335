"""
Title: smith_usersp2.py
Author: Cliff Smith
Date: August 1, 2026
Description: This program connects to the web355DB MongoDB database using
pymongo and performs full CRUD operations (create, read, update, delete)
on a new user document in the users collection.
"""

# Import the MongoClient so we can connect to our MongoDB database
from pymongo import MongoClient
import datetime

# Build a connection string to connect to our web355DB database
client = MongoClient("mongodb+srv://web355_admin:s3cret@bellevueuniversity.brnh6kg.mongodb.net/web355DB")

# Configure a variable to access the web355DB database
db = client['web355DB']

# Step 1: Create a new user document
schumann = {
    "firstName": "Clara",
    "lastName": "Schumann",
    "employeeId": "1013",
    "email": "cschumann@me.com",
    "dateCreated": datetime.datetime.utcnow()
}

# Insert the document into the users collection
schumann_user_id = db.users.insert_one(schumann).inserted_id
print("New user inserted with _id:", schumann_user_id)

# Step 2: Prove the insert worked by searching for the document
print("\nProof of creation:")
print(db.users.find_one({"employeeId": "1013"}))

# Step 3: Update the new user's email address
db.users.update_one(
    {"employeeId": "1013"},
    {"$set": {"email": "clara.schumann@me.com"}}
)

# Step 4: Prove the update worked
print("\nProof of update:")
print(db.users.find_one({"employeeId": "1013"}))

# Step 5: Delete the new user document
db.users.delete_one({"employeeId": "1013"})

# Step 6: Prove the deletion worked (should print None)
print("\nProof of deletion:")
print(db.users.find_one({"employeeId": "1013"}))