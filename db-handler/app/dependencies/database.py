"""Database file that connects to pymongo db"""
from os import environ
import logging

from pymongo import MongoClient, collection, server_api

from app.constants import LOGGER_FORMAT


logging.basicConfig(level=logging.INFO, format=LOGGER_FORMAT)
_LOGGER = logging.getLogger(__name__)
logging.getLogger(__name__).setLevel(logging.DEBUG)

# Grab db details from environment
DB_USER = environ.get('DB_USER')
DB_PASS = environ.get('DB_PASS')

# Information needed for connecting to local db
DB_HOST = 'localhost'
DB_PORT = 27017
DB_NAME = 'mydb'

ARGS = 'retryWrites=true&w=majority&tls=true&tlsCAFile=app/cert.pem'

# URI for mongodb cluster hosted on mongodb atlas
uri = f'mongodb+srv://lambdadb:{DB_PASS}@lambdacluster.vch8k4d.mongodb.net/?{ARGS}'

client: MongoClient = MongoClient(uri, server_api=server_api.ServerApi('1'))

try:
    client.admin.command('ping')
    _LOGGER.info("Connected to hosted database successfully")
except Exception as e:
    print(e)
    _LOGGER.error("Couldn't connect to hosted database")
    _LOGGER.info("Connecting to local database")
    client = MongoClient(DB_HOST, DB_PORT)

cal_col: collection = client[DB_NAME]['calendar']
user_col: collection = client[DB_NAME]['users']
