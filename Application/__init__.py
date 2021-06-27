from flask import Flask
from flask_restful import Api
from Application.api.main_app import CreatePDF
from Application.createdb import mydb

app = Flask(__name__)
api = Api(app)

api.add_resource(CreatePDF, '/api/createpdf/showservicedocument/<id>','/api/createpdf/servicedocument')

mydb.connect()