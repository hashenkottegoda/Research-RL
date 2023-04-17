from flask import Flask, request, jsonify
from mealRuleEngineAPI import getNitrogenReq
import pymongo
client = pymongo.MongoClient("mongodb+srv://y4s1assignments:5bdk2OiVOb4DIKVi@cluster0.m94hxjb.mongodb.net/?retryWrites=true&w=majority")
db = client["Dog_Care_Research"]
dogCollection = db["Dogs"]
from bson import ObjectId, json_util

app = Flask(__name__)

@app.route('/health')
def hello():
    getNitrogenReq()
    return 'Container up and running!'

@app.route('/dog/create', methods=['POST'])
def createDog():
    # Insert a document into the collection and handle the error
    try:
        dogCollection.insert_one(request.json)
        return jsonify({"message": "dog inserted successfully!"})
    except Exception as error:
        return f"Error: {error}"
    
@app.route('/dog/update/<string:id>', methods=['PUT'])
def updateDog(id):
    try:
        dogCollection.update_one(({"_id": ObjectId(id)}), {"$set": request.json})
        return jsonify({"message": "dog updated successfully!"})
    except Exception as error:
        return f"Error: {error}"

@app.route('/dog/<string:id>', methods=['GET'])
def getDog(id):
    # Get a document from the collection and handle the error
    try:
        dog = dogCollection.find_one({"_id": ObjectId(id)})
        dog = json_util.dumps(dog)

        return jsonify(dog)
    except Exception as error:
        return f"Error: {error}"
    
if __name__ == '__main__':
    app.run()
