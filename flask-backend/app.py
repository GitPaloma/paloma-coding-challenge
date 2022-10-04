import os
from flask import Flask, render_template, json, current_app as app
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

filename = os.path.join(app.root_path, 'titles.json')
with open(filename) as file:
    mock_data = json.load(file)

@app.route('/api/content', methods=["GET"])
def index():
    return mock_data

@app.route('/api/titles/series', methods=["GET"])
@cross_origin(supports_credentials=True)
def series():
    return [title for title in mock_data['entries'] if title['programType'] == "series"]

@app.route('/api/titles/movies', methods=["GET"])
@cross_origin(supports_credentials=True)
def movies():
    return [title for title in mock_data['entries'] if title['programType'] == "movie"]
