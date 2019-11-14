import connexion
import pymongo
from bson.json_util import dumps

client = pymongo.MongoClient(
    "mongodb+srv://distribuidos:Distribuidos20192@distribuidos-1rmzz.mongodb.net/test?retryWrites=true&w=majority")

def get_users():

    db = client.distribuidos
    cursor = db.users.find()

    return dumps(cursor)

def get_user(username):
    db = client.distribuidos
    cursor = db.users.find_one(
        {
            "username": username,
        }
    )
    return dumps(cursor)

def insert_user(username):
    db = client.distribuidos
    user_id = 1
    db.users.insert_one(
        {
            "id": user_id,
            "username": username,
        }
    )
    return get_user(username)

def delete_user(username):

    db = client.distribuidos
    db.users.delete_one(
        {
            "username": username,
        }
    )
    return "Se ha borrado el usuario con éxito"

if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, port=5000, specification_dir='openapi/')
    app.add_api('indexer.yaml', arguments={'title': 'user api'})
    app.run()
