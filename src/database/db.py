# Setting up the database
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')

# Delete the database 'xharktank' if present and create a new one
dbs = client.list_database_names()
if 'xharktank' in dbs:
    client.drop_database('xharktank')

database = client.xharktank
collection = database.pitches