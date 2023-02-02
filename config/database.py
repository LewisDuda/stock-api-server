from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
DB_URL = os.getenv("DB_URL")
DB_COLLECTION = os.getenv("DB_COLLECTION")


def database_config(collectionName):
    print('tt', DB_URL, DB_COLLECTION)
    db = MongoClient(DB_URL)[DB_COLLECTION]
    collection = db[collectionName]
    return collection
