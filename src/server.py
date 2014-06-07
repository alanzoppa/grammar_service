from flask import Flask, request, Response, jsonify, json
app = Flask(__name__)
from ipdb import set_trace
from document import Document

class InvalidUsage(Exception):
    def __init__(self, message, status_code=400):
        super(InvalidUsage, self).__init__()
        self.message = message
        self.status_code = status_code

class JSONParseException(InvalidUsage):
    pass

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify({'error': error.message})
    response.status_code = error.status_code
    return response


@app.route('/', methods=['POST'])
def hello_world():
    if request.method == "POST":
        try:
            data = json.loads(request.data)
            documents = [Document(document).tagged_document() for document in data['documents']]
        except ValueError as err:
            raise JSONParseException(str(err), 500)
        except Exception as err:
            raise InvalidUsage(str(err), 500)
        return jsonify({'documents': documents})

if __name__ == '__main__':
    app.run(debug=True)
