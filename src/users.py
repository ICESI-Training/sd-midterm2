import pymongo
from bson.json_util import dumps

users = {
    "JesusPaz": {
        "name": "Jesus 1",
        "numRepos": 2
    },
    "Jesus2": {
        "name": "Jesus 2",
        "numRepos": 3
    },
    "Jesus3": {
        "name": "Jesus 3",
        "numRepos": 4
    }
}

MongoDB_URI = "mongodb+srv://jesuspaz:admin@cluster0-sobp3.mongodb.net/sd?retryWrites=true&w=majority"
client = pymongo.MongoClient(MongoDB_URI)
db = client.get_default_database()
users = db['users']


# Return all the users from the database, you can access using a GET /users
def read():
    return dumps(users.find())

def insert(name):
    result = users.insert_one({"name": name, "numRepos": 4})
    return dumps(result.inserted_id)
