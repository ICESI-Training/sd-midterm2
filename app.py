from flask import render_template
import connexion

app = connexion.FlaskApp(__name__, specification_dir='./')

app.add_api('swagger.yml')

@app.route('/')
def home():
    return "Welcome to my API"

if __name__ == '__main__':
    app.run(threaded=True, debug=True)