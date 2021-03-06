from flask import Flask, request

app = Flask(__name__)


@app.route('/logs', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        return 'it receives a log object to save'
    else:
        return 'it renders logs list'
