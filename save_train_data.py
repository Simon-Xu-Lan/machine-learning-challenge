import pymongo
from config import ATLAS_PASSWORD


# MongoDB
atlas_conn = f'mongodb+srv://simon:{ATLAS_PASSWORD}@cluster0.23jm7.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

def save_train_data(data):
    with pymongo.MongoClient(atlas_conn) as client:
                db = client.handwriting_DB
                collection = db.training_data
                collection.insert_one(data)

