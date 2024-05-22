from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()

uri = os.getenv("DB_URI")
name = os.getenv("DB_NAME")

# MongoDB connection
client = MongoClient(uri)

db = client.get_database(name)

# Tasks Collection
tasks_collection = db["Tasks"]

# Users Collection
users_collection = db["Users"]

# Projects Collection
projects_collection = db["Projects"]

comments_collection = db["Comments"]

attachments_collection = db["Attachments"]
