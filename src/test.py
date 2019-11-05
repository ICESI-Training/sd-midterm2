import pymongo

client = pymongo.MongoClient("mongodb+srv://jesuspaz:admin@cluster0-sobp3.mongodb.net/test?retryWrites=true&w=majority")
db = client.get_default_database()
users = db['users']
#users.insert_one({"hola":"mundo"})
cursor = users.find({})
for doc in cursor:
    print(doc)
client.close()