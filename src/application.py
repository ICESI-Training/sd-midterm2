from flask import render_template
import connexion
from flask_cors import CORS

application = app = connexion.FlaskApp(__name__, specification_dir='./')

cors = CORS(app.app)

app.add_api('swagger.yml')
app.debug=True

@app.route('/')
def home():
    return "Welcome to my API"

if __name__ == '__main__':
    app.run(host='localhost')
