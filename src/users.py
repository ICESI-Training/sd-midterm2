import pymongo
from bson.json_util import dumps
import requests
import json

MongoDB_URI = "mongodb+srv://admin:admin@cluster0-n5sgi.mongodb.net/sd-db?retryWrites=true&w=majority"
client = pymongo.MongoClient(MongoDB_URI)
db = client.get_default_database()
users = db['users']

urlBase = 'https://api.github.com'

# Return all the users from the database, you can access using a GET /users
def read():
    return dumps(users.find())

def insert(name):
    r = requests.get(urlBase+"/users/"+name)
    response = json.loads(r.content)
    numRepos = response["public_repos"]
    result = users.insert_one({"name": name, "numRepos": numRepos})
    data = {"id" : result.inserted_id, "numRepos" : numRepos}
    return dumps(data)
