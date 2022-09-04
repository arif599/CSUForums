from flask import Flask, request, jsonify
from flask_restful import Api, Resource

from Models.users import Users



app = Flask(__name__)
api = Api(app)
# https://stackoverflow.com/questions/30491841/python-flask-restful-post-not-taking-json-arguments
class UserAPI(Resource):
    def get(self):
        return {'id': id}

    def post(self):
        json_data = request.get_json(force=True)
        username = json_data['username']
        password = json_data['password']
        Users(username, password)
        return jsonify(username=username, password=password)

    def delete(self, id):
        pass

api.add_resource(UserAPI, '/users/', endpoint = 'user')

if __name__ == '__main__':
    app.run(debug=True)