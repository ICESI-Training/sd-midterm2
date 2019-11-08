from flask import render_template
import connexion

application = app = connexion.FlaskApp(__name__, specification_dir='./')

app.add_api('swagger.yml')
app.debug=True

@app.route('/')
def home():
    return "Welcome to my API"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
