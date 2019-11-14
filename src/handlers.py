import connexion

def get_user_info(username):
    
    import pymongo
    from bson.json_util import dumps
    
    client = pymongo.MongoClient("mongodb+srv://distribuidos:Distribuidos20192@distribuidos-1rmzz.mongodb.net/test?retryWrites=true&w=majority")
    db = client.sample_supplies
    cursor = db.sales.find()

    return dumps(cursor)

    #return {'username': col, 'id': '123', 'role': 'admin'}

def get_commits(username, start_date, end_date):
    return 'commits list'

if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, port=5000, specification_dir='openapi/')
    app.add_api('indexer.yaml', arguments={'title': 'user api'})
    app.run()