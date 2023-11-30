from flask import Flask, request
from DataBase import db,app

from DataBase import Employees


#app = Flask(__name__)

#db = Connection(app,"postgresql+psycopg2://postgres:november@127.0.0.1:5432/CompanyData")

@app.route('/employees')
def get_all_employees():
    employees = Employees.query.all()
    print(employees)
    employees = [employee.to_dict() for employee in employees]
    return {"data": employees}

@app.route('/employee/<id>', methods=['GET', 'DELETE'])
def get_employee(id):
    employee = Employees.query.get_or_404(id)
    if request.method == 'GET':
        
        print(employee)
        #employees = [employee.to_dict() for employee in employees]
        return {"data": employee.to_dict() }
    elif request.method == 'DELETE':
        print(f'Delete {id}')
        db.session.delete(employee)
        db.session.commit()
        return {"message": f"Person {employee.name} successfully deleted."}

@app.route('/employee', methods=["POST"])
def add_employee():
    body = request.json
    employee = Employees(**body)

    db.session.add(employee)
    db.session.commit()
    return {"message": "New employee added successfully"}



app.run()
