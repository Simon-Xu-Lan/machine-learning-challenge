import pymongo
from bson.objectid import ObjectId
from config import ATLAS_PASSWORD


# MongoDB
atlas_conn = f'mongodb+srv://simon:{ATLAS_PASSWORD}@cluster0.23jm7.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

def clear_train_data(id):
    with pymongo.MongoClient(atlas_conn) as client:
                db = client.handwriting_DB
                collection = db.training_data
                collection.delete_one({"_id": ObjectId(id)})