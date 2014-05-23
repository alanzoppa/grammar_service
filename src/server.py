from flask import Flask, request, Response, jsonify
app = Flask(__name__)
from pudb import set_trace

class InvalidUsage(Exception):
    def __init__(self, message):
        super(InvalidUsage, self).__init__()
        self.message = message

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify({'error': error.message})
    response.content_type = 'application/vnd.api+json'
    response.status_code = 400
    return response

@app.route('/', methods=['POST'])
def hello_world():
    if request.content_type != 'application/vnd.api+json':
        raise InvalidUsage("use application/vnd.api+json")
    if request.method == "POST":
        return Response("Post", mimetype='application/vnd.api+json')

if __name__ == '__main__':
    app.run(debug=True)
