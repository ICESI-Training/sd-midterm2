'''
    You need to install using pip:
        - flask
        - connexion[swagger-ui]
        - pymongo
        - dnspython

        jesuspaz    
        GiyTG0yMsM2VCyJq
'''
from flask import render_template
import connexion

app = connexion.FlaskApp(__name__, specification_dir='./')

app.add_api('swagger.yml')

@app.route('/')
def home():
    return {"Hello": "To Home"}

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)