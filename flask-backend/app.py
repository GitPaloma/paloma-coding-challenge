import os

from flask import Flask, json
from flask_cors import CORS, cross_origin
from flask_migrate import Migrate

from db import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app, support_credentials=True)
db.init_app(app)
Migrate(app, db)

filename = 'titles.json'
with open(filename) as file:
    mock_data = json.load(file)



@app.route('/api/content', methods=["GET"])
@cross_origin(supports_credentials=True)
def index():
    return mock_data
