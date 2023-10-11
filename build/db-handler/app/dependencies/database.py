from pymongo import MongoClient, collection, server_api
from os import environ

DB_USER = environ.get("DB_USER")
DB_PASS = environ.get("DB_PASS")

DB_HOST = "localhost"
DB_PORT = 27017
DB_NAME = "mydb"

args = "retryWrites=true&w=majority&tls=true&tlsCAFile=app/cert.pem"
uri = f"mongodb+srv://lambdadb:{DB_PASS}@lambdacluster.vch8k4d.mongodb.net/?{args}"

client: MongoClient = MongoClient(uri, server_api=server_api.ServerApi("1"))

try:
    client.admin.command("ping")
    print("SUCCESSFUL - CONNECTING TO CLOUD DB")
except Exception as e:
    print(e)
    print("UNSUCCESSFUL - CONNECTING TO CLOUD DB")
    print("SUCCESSFUL - SWAPPING TO LOCAL DB")
    client = MongoClient(DB_HOST, DB_PORT)

cal_col: collection = client[DB_NAME]["calendar"]
user_col: collection = client[DB_NAME]["users"]
