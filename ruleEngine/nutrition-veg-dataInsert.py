import pymongo
client = pymongo.MongoClient("mongodb+srv://y4s1assignments:5bdk2OiVOb4DIKVi@cluster0.m94hxjb.mongodb.net/?retryWrites=true&w=majority")
db = client["Dog_Care_Research"]
collection = db["Vegetables"]

# Check if the connection to the MongoDB instance is successful
try:
    # The ismaster command is used to check the connection
    client.admin.command('ismaster')
    print("Connection successful!")
except pymongo.errors.ServerSelectionTimeoutError as error:
    print(f"Connection failed: {error}")

# Insert a document into the collection
records = [
    {"name": "sweet potatoes", "category": "vegetables", "p":1.6, "f": 0.1, "c":20, "ckl":86}, 
    {"name": "carrots", "category": "vegetables" , "p":0.9, "f":0.2, "c":10, "ckl":41 },
    {"name": "green beans", "category": "vegetables" , "p":1.8, "f":0.1, "c":7, "ckl":31},
    {"name": "brocolli", "category": "vegetables", "p":2.8, "f":0.4, "c":7 , "ckl": 34},
    {"name": "spinach", "category": "vegetables", "p":2.9, "f":0.4, "c":3.6 , "ckl":23},
    {"name": "pumpkin", "category": "vegetables", "p":1, "f":0.1 , "c":7, "ckl": 26},
]
collection.insert_many(records)
print("Document inserted successfully!")