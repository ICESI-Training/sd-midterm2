from pymongo import MongoClient

client = MongoClient("mongodb+srv://prueba:prueba123@cluster0-vba48.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
DEBUG = True
