from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

db_user = os.environ['MONGO_DB_USER']
db_pass = os.environ['MONGO_DB_PASSWORD']


def get_database():
    CONNECTION_STRING = f"mongodb+srv://{db_user}:{db_pass}@playground.xvsgupa.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)
    return client['user_shopping_list']


if __name__ == "__main__":
    dbname = get_database()
