import pymongo
client = pymongo.MongoClient("mongodb+srv://y4s1assignments:5bdk2OiVOb4DIKVi@cluster0.m94hxjb.mongodb.net/?retryWrites=true&w=majority")
db = client["Dog_Care_Research"]
collection = db["Carbohydrates"]

# Check if the connection to the MongoDB instance is successful
try:
    # The ismaster command is used to check the connection
    client.admin.command('ismaster')
    print("Connection successful!")
except pymongo.errors.ServerSelectionTimeoutError as error:
    print(f"Connection failed: {error}")

# Insert a document into the collection
records = [
    {"name": "oats", "category": "whole grains", "p": 11.1, "f": 6.9, "c":62.4, "ckl":379}, 
    {"name": "barley", "category": "whole grains", "p":12, "f":2.3, "c":73, "ckl":354}, 
    {"name": "brown rice", "category": "whole grains", "p":2.6, "f":0.9, "c":23, "ckl":111}, 
    {"name": "quinoa", "category": "whole grains", "p":3.54, "f":1.8, "c":25.22, "ckl":112}
]
collection.insert_many(records)
print("Document inserted successfully!")