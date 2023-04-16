import pymongo
client = pymongo.MongoClient("mongodb+srv://y4s1assignments:5bdk2OiVOb4DIKVi@cluster0.m94hxjb.mongodb.net/?retryWrites=true&w=majority")
db = client["Dog_Care_Research"]
collection = db["Proteins"]

# Check if the connection to the MongoDB instance is successful
try:
    # The ismaster command is used to check the connection
    client.admin.command('ismaster')
    print("Connection successful!")
except pymongo.errors.ServerSelectionTimeoutError as error:
    print(f"Connection failed: {error}")

# Insert a document into the collection
records = [
    {"name": "beef", "category": "meat", "p": 27, "f": 14, "c": 0, "ckl": 239}, 
    {"name": "chicken", "category": "meat", "p": 0, "f": 0, "c": 0, "ckl": 0}, 
    {"name": "lamb", "category": "meat", "p": 0, "f": 0, "c": 0, "ckl": 0}, 
    {"name": "turkey", "category": "meat", "p": 0, "f": 0, "c": 0, "ckl": 0}, 
    {"name": "salmon", "category": "fish", "p": 0, "f": 0, "c": 0, "ckl": 0}, 
    {"name": "tuna", "category": "fish", "p": 0, "f": 0, "c": 0, "ckl": 0}, 
    {"name": "sardines", "category": "fish", "p": 0, "f": 0, "c": 0, "ckl": 0}, 
    {"name": "eggs", "category": "fish", "p": 0, "f": 0, "c": 0, "ckl": 0}, 
    {"name": "soybeans", "category": "plant", "p": 0, "f": 0, "c": 0, "ckl": 0},
    {"name": "lentils", "category": "plant", "p": 0, "f": 0, "c": 0, "ckl": 0}, 
    {"name": "chickpeas", "category": "plant", "p": 0, "f": 0, "c": 0, "ckl": 0},
    {"name": "pease", "category": "plant", "p": 0, "f": 0, "c": 0, "ckl": 0}
]
collection.insert_many(records)
print("Document inserted successfully!")