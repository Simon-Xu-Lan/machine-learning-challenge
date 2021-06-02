from flask.templating import render_template
import pymongo
from config import ATLAS_PASSWORD


# MongoDB
atlas_conn = f'mongodb+srv://simon:{ATLAS_PASSWORD}@cluster0.23jm7.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

def retrieve_train_data():
    with pymongo.MongoClient(atlas_conn) as client:
                db = client.handwriting_DB
                collection = db.training_data
                data = collection.find({})

    return data


