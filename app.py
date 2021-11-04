from flask import Flask, request
from server.user_cli import process_file
import os
import json
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route('/file-upload', methods=['POST'])
def file_upload():
    """
    POST end point for receiving the file send by the client. The file has to be sent as form data with the key file
    :return: HTTP 400 response code if the file data is missing; HTTP 200 response code if the request was successful
    """
    file = request.files['file']
    filename = file.filename
    filetype = filename.split(".")[1]
    if filename == "":
        print("Invalid request data")
        return '400'

    file.save(os.path.join("./data/", filename))
    process_file(filename, filetype)
    return '200'


@app.route('/get-results')
def send_data():
    """
    GET API end point that returns the file details the client requests for.
    The client must send the file name as a query parameters with the key - filename
    :return: HTTP 400 response code if the filename is missing in the query parameters;
             HTTP 404 response code if the file is not found on the server;
             JSON data containing the question - answer pairs for the file
    """
    filename = request.args.get('filename')

    if filename is None:
        print("Invalid query params : {}".format(filename))
        return '400'

    filepath = "./data/results-{}.txt".format(filename)
    try:
        f = open(filepath, "r")
        data = f.read()
        json_data = json.loads(data)
        # response = {"data": json_data}
        # response.headers.add('Access-Control-Allow-Origin', '*')
        return json_data
    except FileNotFoundError:
        print("File Not found : {}".format(filename))
        return '404'


if __name__ == "__main__":
    """
    Starts the flask server on port 5000 in debug mode. This is the entry point for the code.
    """
    app.run(debug=True, port=5000)
