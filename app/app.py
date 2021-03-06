from flask import Flask, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#from .models import Log, Address


@app.route('/logs', methods=['GET', 'POST'])
def logs():
    if request.method == 'POST':
        return 'it receives a log object to save'
    else:
        return 'it renders logs list'


@app.route('/address', methods=['GET'])
def address():
    return 'it renders logs list'


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
