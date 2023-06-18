from flask_restful import Resource, Api, reqparse
from db import example
from flask import Flask

class HelloWorld(Resource):
    def get(self):
        return dict(example.list_examples())

class Query(Resource):
    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument("id", type=str, location='args')
        return parser.parse_args()