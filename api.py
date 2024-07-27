from flask import Flask,request
#we have to install flask_restful.....pip install flask_restful
from flask_restful import Resource,Api # to get tha data 
from flask_restful import reqparse  # to post update 


app = Flask(__name__)
api = Api(app)

# employees = {
#             "E001":{"Name":"sayali","Age":29,"Department" : "IT"},
#             "E002":{"Name":"samyak","Age":30,"Department" : "HR"},
#             "E003":{"Name":"shyamli","Age":24,"Department" : "dev"},
#             "E004":{"Name":"Amol","Age":23,"Department" : "deployee"}
#  }

employees = []

class EmployeeAPI(Resource):
    def get(self):
        return employees

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("ID",type=str, required=True,help="ID cannot be blank")
        parser.add_argument("Name",type=str, required=True, help="Name cannot be blank")
        parser.add_argument("Age",type=int, required=True, help="Age cannot be blank")
        parser.add_argument("Department", type=str , required=True, help="DEpartment cannot be blank")

        data = parser.parse_args()

        for emp in employees:
            if emp['ID'] == data['ID']:
                return {'message' :f"Employee with the name{data['ID']} already exists.!!!" },400

        new_employee = {
            'ID' : data['ID'],
            'Name' : data['Name'],
            'Age' : data['Age'],
            'Department' : data['Department']
        }
        employees.append(new_employee)
        return new_employee,201

class SingleEmployeeAPI(Resource):
    def get(self,emp_id):
        return employees[emp_id]

api.add_resource(EmployeeAPI,'/')
api.add_resource(SingleEmployeeAPI,'/emp/<emp_id>')

app.run(debug=True)