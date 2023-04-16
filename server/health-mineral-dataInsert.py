import pymongo
client = pymongo.MongoClient("mongodb+srv://y4s1assignments:5bdk2OiVOb4DIKVi@cluster0.m94hxjb.mongodb.net/?retryWrites=true&w=majority")
db = client["Dog_Care_Research"]
collection = db["Minerals"]

# Check if the connection to the MongoDB instance is successful
try:
    # The ismaster command is used to check the connection
    client.admin.command('ismaster')
    print("Connection successful!")
except pymongo.errors.ServerSelectionTimeoutError as error:
    print(f"Connection failed: {error}")

# Insert a document into the collection
records = [
    {"rule": "mn_calcium_def", "allowance": 1}, 
    {"rule": "mn_phosphorus_def", "allowance": 0.75}, 
    {"rule": "mn_magnesium_def", "allowance": 150}, 
    {"rule": "mn_sodium_def", "allowance": 200}, 
    {"rule": "mn_potassium_def", "allowance":1}, 
    {"rule": "mn_chlorine_def", "allowance": 300}, 
    {"rule": "mn_iron_def", "allowance": 7.5}, 
    {"rule": "mn_copper_def", "allowance": 1.5}, 
    {"rule": "mn_zink_def", "allowance": 15}, 
    {"rule": "mn_manganese_def", "allowance": 1.2}, 
    {"rule": "mn_selenium_def ", "allowance": 90}, 
    {"rule": "mn_iodine_def", "allowance": 220}, 
]
collection.insert_many(records)
print("Document inserted successfully!")