from flask import Flask ,request
from flask_restful import Resource,reqparse,Api
from pymongo import MongoClient
import json
from bson.objectid import ObjectId
from bson.json_util import dumps

app = Flask(__name__)
api = Api(app)

#mongo_uri ="mongodb+srv://sayalishende:sayali%40123@sayalishende.otpu5gi.mongodb.net/?retryWrites=true&w=majority&appName=sayalishende"
mongo_uri = "mongodb+srv://sayalishende:sayali%40123@sayalishende.otpu5gi.mongodb.net/?retryWrites=true&w=majority&appName=sayalishende"
client = MongoClient(mongo_uri)

db = client['Flask-DB']
collection = db['employees']

class EmployeeAPI(Resource):
    def get(self):
        employees = json.loads(dumps(collection.find({},{'_id':0})))
        return employees,200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("ID",type=int, required=True,help="ID cannot be blank")
        parser.add_argument("Name",type=str, required=True, help="Name cannot be blank")
        parser.add_argument("Age",type=int, required=True, help="Age cannot be blank")
        parser.add_argument("Department", type=str , required=True, help="DEpartment cannot be blank")

        data = parser.parse_args()

        if collection.find_one({'ID':data['ID']}):
                return {'message' :f"Employee with the ID {data['ID']} already exists.!!!" },400

        new_employee = {
            'ID' : data['ID'],
            'Name' : data['Name'],
            'Age' : data['Age'],
            'Department' : data['Department']
        }
        #employees.append(new_employee)
        result=collection.insert_one(new_employee)
        new_employee['_id'] = str(result.inserted_id)
        return new_employee,201

class SingleEmployeeAPI(Resource):
    def get(self, ID):
        employee = collection.find_one({'ID':int(ID)}) 
        if employee:
            employee['_id'] = str(employee['_id'])
            return json.loads(dumps(employee)),200
        return {message:'Employee not found'},404

    def delete(self,ID):
        employee = collection.find_one({'ID':int(ID)})
        if employee:
            collection.delete_one({'ID':int(ID)})
            return {'message':'Employee deleted successfully'},200
        return {'message':'Employee not found'},404

    def put(self,ID):
        data = request.get_json()
        employee = collection.find_one({'ID':int(ID)})
        if not employee:
            return {'message': 'Empolyee not found'},404

        updated_employee = {
            'Name' : data['Name'],
            'Age' : data['Age'],
            'Department' : data['Department']
        }
        collection.update_one({'ID': int(ID)},{'$set': updated_employee})
        updated_employee['ID'] = int(ID)
        return {'message': 'Employee Updated Successfully'},200

api.add_resource(EmployeeAPI,'/')
api.add_resource(SingleEmployeeAPI,'/employees/<int:ID>')



app.run(debug=True)
