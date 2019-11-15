import connexion
import pymongo
from bson.json_util import dumps

client = pymongo.MongoClient(
    "mongodb+srv://distribuidos:Distribuidos20192@distribuidos-1rmzz.mongodb.net/test?retryWrites=true&w=majority")
db = client.distribuidos

def get_users():

    user = db.users.find()

    return dumps(user)

def get_user(cc):
    if(cc.strip()):
        user = db.users.find_one(
            {
                "cc": cc,
            }
        )
        if(user is not None):
            return dumps(user)
        else:
            return 'Not found', 404, {
                'exists-error': 'The user with the given cc was not found'
            }
    else:
        return 'Bad Request', 400, {
            'empty-error': 'The cc parameter must not be empty'
        }

def insert_user(cc,username):
    if(cc.strip()):
        if(username.strip()):
            user = db.users.find_one({"cc": cc,})
            if(user is None):
                db.users.insert_one(
                    {
                        "cc": cc,
                        "username": username,
                    }
                )
                return 201
            else:
                return 'Bad Request', 400, {
                    'exists-error': 'The user with the given cc already exists'
                }   

        else:
            return 'Bad Request', 400, {
                'empty-error': 'The username parameter must not be empty'
            }
    else:
        return 'Bad Request', 400, {
            'empty-error': 'The cc parameter must not be empty'
        }

def delete_user(cc):
    if(cc.strip()):
        user = db.users.find_one({"cc": cc,})
        if(user is not None):
            db.users.delete_one(
                {
                    "cc": cc,
                }
            )
            return 200
        else:
            return 'Not found', 404, {
                'exists-error': 'The user with the given cc was not found'
            }
    else:
        return 'Bad Request', 400, {
            'empty-error': 'The cc parameter must not be empty'
        }

if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, port=5000, specification_dir='openapi/')
    app.add_api('indexer.yaml', arguments={'title': 'user api'})
    app.run()
