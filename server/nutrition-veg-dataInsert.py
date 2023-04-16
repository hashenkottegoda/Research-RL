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
    {"name": "sweet potatoes", "category": "vegetables", "p": 0, "f": 0, "c": 0, "ckl": 0}, 
    {"name": "carrots", "category": "vegetables" , "p": 0, "f": 0, "c": 0, "ckl": 0},
    {"name": "green beans", "category": "vegetables" , "p": 0, "f": 0, "c": 0, "ckl": 0},
    {"name": "brocolli", "category": "vegetables", "p": 0, "f": 0, "c": 0, "ckl": 0},
    {"name": "spinach", "category": "vegetables", "p": 0, "f": 0, "c": 0, "ckl": 0},
    {"name": "pumpkin", "category": "vegetables", "p": 0, "f": 0, "c": 0, "ckl": 0},
]
collection.insert_many(records)
print("Document inserted successfully!")