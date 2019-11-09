import pymongo
from bson.json_util import dumps
import requests
import json
import dns
import os

url = os.environ.get("mongoURL")+"/sd-db?retryWrites=true&w=majority"
client = pymongo.MongoClient(url)

db = client.get_default_database()
users = db['users']

urlBase = 'https://api.github.com'


# Return all the users from the database, you can access using a GET /users
def read():
    return dumps(users.find())


def insert(name):
    # User name is empty
    if name.strip() != "":
        # Users exists in the data base

        if users.find({"name": name}).count() == 0:

            r = requests.get(urlBase + "/users/" + name)
            # Users is a github user
            if r.status_code == 200:
                response = json.loads(r.content)
                numRepos = response["public_repos"]
                result = users.insert_one({"name": name, "numRepos": numRepos})
                data = {"id": result.inserted_id, "numRepos": numRepos}
                return dumps(data)
            else:
                return 'Bad request', 400, {
                    'exists-gh-error':
                    'The name of the user given is not in the GitHub database'
                }
        else:
            return 'Bad request', 400, {
                'exists-error': 'The users exists in the database'
            }
    else:
        return 'Bad request', 400, {
            'empty-error': 'The name of the user given can not be empty'
        }


def delete(name):
    # User name is empty
    if name.strip() != "":

        # Users exists in the data base
        if users.find({"name": name}).count() == 1:

            users.remove({"name": name})
            return 200
        else:
            return 'Bad request', 400, {
                'exists-error': 'The users do not exists in the database'
            }
    else:
        return 'Bad request', 400, {
            'empty-error': 'The name of the user given can not be empty'
        }
