import pymongo
client = pymongo.MongoClient("mongodb+srv://y4s1assignments:5bdk2OiVOb4DIKVi@cluster0.m94hxjb.mongodb.net/?retryWrites=true&w=majority")
db = client["Dog_Care_Research"]
collection = db["Vitamins"]

# Check if the connection to the MongoDB instance is successful
try:
    # The ismaster command is used to check the connection
    client.admin.command('ismaster')
    print("Connection successful!")
except pymongo.errors.ServerSelectionTimeoutError as error:
    print(f"Connection failed: {error}")

# Insert a document into the collection
records = [
    {"rule": "vit_a_def", "allowance": 379}, 
    {"rule": "vit_d_def", "allowance": 3.4}, 
    {"rule": "vit_e_def", "allowance": 8}, 
    {"rule": "vit_k_def", "allowance": 0.41}, 
    {"rule": "vit_b1_def", "allowance":0.56}, 
    {"rule": "vit_riboflavin_def", "allowance": 1.3}, 
    {"rule": "vit_b6_def", "allowance": 0.4}, 
    {"rule": "vit_niacin_def", "allowance": 4}, 
    {"rule": "vit_pantothenicAcid_def", "allowance": 4}, 
    {"rule": "vit_b12_def", "allowance": 9}, 
    {"rule": "vit_folicAcid_def", "allowance":68 }, 
    {"rule": "vit_choline_def", "allowance": 425}, 
]
collection.insert_many(records)
print("Document inserted successfully!")