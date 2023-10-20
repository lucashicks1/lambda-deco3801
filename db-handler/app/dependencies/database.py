"""Database file that connects to pymongo db"""
from os import environ
import sys
import logging

from pymongo import MongoClient, collection, server_api
from pymongo.errors import ServerSelectionTimeoutError

from app.constants import LOGGER_FORMAT


# Configures logger to show debug messages
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

# Args to use for remote connection
ARGS = 'retryWrites=true&w=majority&tls=true&tlsCAFile=app/cert.pem'

# URI for mongodb cluster hosted on mongodb atlas
uri = f'mongodb+srv://lambdadb:{DB_PASS}@lambdacluster.vch8k4d.mongodb.net/?{ARGS}'

client: MongoClient = MongoClient(uri, server_api=server_api.ServerApi('1'))

# Try to connect to remote client, if not connect to remote 
try:
    if DB_USER is None or DB_PASS is None:
        _LOGGER.error("Username and password from environment is blank")
        raise ValueError()
    client.admin.command('ping')
    _LOGGER.info("Connected to hosted database successfully")
except Exception as e:
    print(e)
    _LOGGER.error("Couldn't connect to hosted database")
    try:
        _LOGGER.info("Connecting to local database")
        client = MongoClient(DB_HOST, DB_PORT, serverSelectionTimeoutMS=10000)
        client.admin.commad('ping')
    except (Exception, ServerSelectionTimeoutError) as ex:
        _LOGGER.error("Error connecting to the local database. Connection timed out")
        sys.exit()


cal_col: collection = client[DB_NAME]['calendar']
user_col: collection = client[DB_NAME]['users']
