from flask_restful import reqparse, abort, Resource
from Application.createdb import mydb
from flask import jsonify
from Application.pdf_creator.service_doc_pdf import  extract_information
from pathlib import Path


parser = reqparse.RequestParser()
parser.add_argument('id')
parser.add_argument('documentdate')
parser.add_argument('clientname')
parser.add_argument('clientaddress')
parser.add_argument('employeename')
parser.add_argument('employeenumber')
parser.add_argument('devicetype')
parser.add_argument('devicebrand')
parser.add_argument('devicemodel')
parser.add_argument('descr')
parser.add_argument('internaldocumentid')

class CreatePDF(Resource):
    def get(self, id):
        curr = mydb.cursor()
        curr.execute(f"SELECT * FROM SERVICEDOCUMENT WHERE ID={id}")
        row = curr.fetchone()
        return jsonify(document=row)

    def post(self):
        args = parser.parse_args()
        documentdate = {'documentdate' : args['documentdate']}
        clientname = {'clientname' : args['clientname']}
        clientaddress = {'clientaddress' : args['clientaddress']}
        employeename = {'employeename' : args['employeename']}
        employeenumber = {'employeenumber' : args['employeenumber']}
        devicetype = {'devicetype' : args['devicetype']}
        devicebrand = {'devicebrand' : args['devicebrand']}
        devicemodel = {'devicemodel' : args['devicemodel']}
        descr = {'descr' : args['descr']}
        internaldocumentid = {'internaldocumentid' : args['internaldocumentid']}
        pdf = extract_information(
            documentdate=documentdate, 
            clientname=clientname, 
            clientaddress=clientaddress,
            employeename=employeename,
            employeenumber=employeenumber,
            devicetype=devicetype,
            devicebrand=devicebrand,
            devicemodel=devicemodel,
            descr=descr,
            internaldocumentid=internaldocumentid
            )
        Path(f"D:\\Temp\\Itserwis\\documents\\{args['internaldocumentid']}.pdf").write_bytes(pdf)
        return 'Document saved to pdf', 201
