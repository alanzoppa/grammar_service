from flask import Flask, request, Response, jsonify
app = Flask(__name__)
from pudb import set_trace
import pyringe

class InvalidUsage(Exception):
    pass

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify({'error': 'use application/vnd.api+json'})
    response.content_type = 'application/vnd.api+json'
    response.status_code = 400
    return response

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    #pyringe.interact()
    if request.content_type != 'application/vnd.api+json':
        raise InvalidUsage()
    if request.method == "POST":
        return Response("Post", mimetype='application/vnd.api+json')
        
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)
