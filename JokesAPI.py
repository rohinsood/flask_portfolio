from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
from model_jokes import * # import the model_jokes.py file
import requests  # used for testing 
import random

# Blueprints allow this code to be procedurally abstracted from main.py, meaning code is not all in one place
app_api = Blueprint('api', __name__,
                   url_prefix='/api/jokes')  # endpoint prefix avoid redundantly typing /api/jokes over and over

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(app_api)

class JokesAPI:
    # not implemented, this would be where we would allow creation of a new Joke
    class _Create(Resource):
        def post(self, joke):
            pass
            
    # getJokes()
    class _Read(Resource):
        def get(self):
            return jsonify(getJokes())

    # getJoke(id)
    class _ReadID(Resource):
        def get(self, id):
            return jsonify(getJoke(id))

    # getRandomJoke()
    class _ReadRandom(Resource):
        def get(self):
            return jsonify(getRandomJoke())
    
    # getRandomJoke()
    class _ReadCount(Resource):
        def get(self):
            count = countJokes()
            countMsg = {'count': count}
            return jsonify(countMsg)

    # put method: addJokeHaHa
    class _UpdateLike(Resource):
        def put(self, id):
            addJokeHaHa(id)
            return jsonify(getJoke(id))

    # put method: addJokeBooHoo
    class _UpdateJeer(Resource):
        def put(self, id):
            addJokeBooHoo(id)
            return jsonify(getJoke(id))

    # building RESTapi interfaces, these routes are added to Web Server http://<server</api/jokes
    api.add_resource(_Create, '/create/<string:joke>')
    api.add_resource(_Read, '/')    # default, which returns all jokes
    api.add_resource(_ReadID, '/<int:id>')
    api.add_resource(_ReadRandom, '/random')
    api.add_resource(_ReadCount, '/count')
    api.add_resource(_UpdateLike, '/like/<int:id>/')
    api.add_resource(_UpdateJeer, '/jeer/<int:id>/')
