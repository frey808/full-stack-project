from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS

from server.api.skate import *
from server.db.setup import *

app = Flask(__name__) #create Flask instance
CORS(app) #Enable CORS on Flask server to work with Nodejs pages
api = Api(app) #api router

api.add_resource(Data,'/load')
api.add_resource(Edit,'/edit')

if __name__ == '__main__':
    print("Loading db")
    rebuild()
    print("Starting flask")
    app.run(debug=True)