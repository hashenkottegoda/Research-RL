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
    {"name": "beef", "category": "meat", "p":26 , "f":15, "c": 0, "ckl": 250}, 
    {"name": "chicken", "category": "meat", "p": 27, "f":14, "c":0, "ckl":239}, 
    {"name": "lamb", "category": "meat", "p":25, "f":21, "c":0, "ckl":294}, 
    {"name": "turkey", "category": "meat", "p":29 , "f":7, "c":0,"ckl":189}, 
    {"name": "salmon", "category": "fish", "p":20, "f":13, "c": 0, "ckl": 208}, 
    {"name": "tuna", "category": "fish", "p":28, "f":1.3, "c":0, "ckl":132}, 
    {"name": "sardines", "category": "fish", "p":19.8 , "f":11, "c":0, "ckl":129}, 
    {"name": "eggs", "category": "fish", "p":13, "f":11, "c":1.1, "ckl":155}, 
    {"name": "soybeans", "category": "plant", "p":36, "f":20, "c":30, "ckl":446},
    {"name": "lentils", "category": "plant", "p":9, "f":0.4, "c":20, "ckl":116}, 
    {"name": "chickpeas", "category": "plant", "p":19, "f":6, "c":61, "ckl":364},
    {"name": "pease", "category": "plant", "p":5, "f":0.4, "c":14, "ckl":81}
]
collection.insert_many(records)
print("Document inserted successfully!")