from pymongo import MongoClient, collection

DB_HOST = "localhost"
DB_PORT = 27017
DB_NAME = "mydb"
COL_NAME = "calendar"

client = MongoClient(DB_HOST, DB_PORT)

cal_col: collection = client[DB_NAME][COL_NAME]
