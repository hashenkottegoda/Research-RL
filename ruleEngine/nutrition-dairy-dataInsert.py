import pymongo
client = pymongo.MongoClient("mongodb+srv://y4s1assignments:5bdk2OiVOb4DIKVi@cluster0.m94hxjb.mongodb.net/?retryWrites=true&w=majority")
db = client["Dog_Care_Research"]
collection = db["Dairy"]

# Check if the connection to the MongoDB instance is successful
try:
    # The ismaster command is used to check the connection
    client.admin.command('ismaster')
    print("Connection successful!")
except pymongo.errors.ServerSelectionTimeoutError as error:
    print(f"Connection failed: {error}")

# Insert a document into the collection
records = [
    {"name": "milk", "category": "dairy", "p": 3, "f": 1, "c": 5, "ckl":44}, 
    {"name": "yoghurt", "category": "dairy" , "p":10, "f":0.4, "c":3.6 , "ckl":59},
    {"name": "cheese", "category": "dairy" , "p":25 , "f":33, "c":1.3, "ckl":402},
    {"name": "cottage cheese", "category": "dairy", "p":11, "f":4.3, "c":3.4, "ckl":98}
]
collection.insert_many(records)
print("Document inserted successfully!")