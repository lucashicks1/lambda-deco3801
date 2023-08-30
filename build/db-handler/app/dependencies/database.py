from pymongo import MongoClient, collection

DB_HOST = "localhost"
DB_PORT = 27017
DB_NAME = "mydb"

client = MongoClient(DB_HOST, DB_PORT)

cal_col: collection = client[DB_NAME]["calendar"]
user_col: collection = client[DB_NAME]["users"]
