from flask import Flask, request
from server.user_cli import process_file
import os
import json
app = Flask(__name__)


@app.route('/file-upload', methods=['POST'])
def file_upload():
    file = request.files['file']
    filename = file.filename
    file.save(os.path.join("./data/", filename))
    process_file(filename)
    return 'OK'


@app.route('/get-results')
def send_data():
    filename = request.args.get('filename')
    filepath = "./data/results-{}.txt".format(filename)
    f = open(filepath, "r")
    data = f.read()
    json_data = json.loads(data)
    return json_data


@app.route("/")
def index():
    return "Hello World!"

