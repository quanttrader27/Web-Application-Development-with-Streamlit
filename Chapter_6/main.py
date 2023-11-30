from flask import Flask, request

from DataBase import Employees
from DataBase import *

app = Flask(__name__)


@app.route('/employees')
def get_all_employees():
    employees = Employees.query.all()
    employees = [employee.to_dict() for employee in employees]
    return {"data": employees}


@app.route('/employee', methods=["POST"])
def add_employee():
    body = request.json
    employee = Employees(**body)

    db.session.add(employee)
    db.session.commit()
    return {"message": "New employee added successfully"}



app.run()
