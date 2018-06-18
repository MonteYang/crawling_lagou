from pymongo import MongoClient

client = MongoClient()
db = client.test_database
collection = db.test
collection.insert({'name':'YMN','age':23})