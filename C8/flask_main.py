from flask import Flask, request
from DataBase import Employees, Admins,db,app
from Services import JWTService, HashingService
from DataBase.Middleware import Middleware
from werkzeug import exceptions
import yaml

with open("secrets.yaml") as f:
    yaml_dict = yaml.safe_load(f)
    sing_up_key = yaml_dict['sing_up_key']
    jwt_secret = yaml_dict['jwt_secret']
    print(f'sing_up_key:{sing_up_key} | jwt_secret:{jwt_secret}')

jwt_service = JWTService(jwt_secret)
middleware = Middleware(jwt_service)
hashing_service = HashingService()

app.before_request(lambda: middleware.auth(request))


@app.route('/api/employees')
def get_all_employees():
    employees = Employees.query.all()
    print(employees)
    employees = [employee.to_dict() for employee in employees]
    return {"data": employees}


@app.route('/api/employee', methods=["POST"])
def add_employee():
    body = request.json
    employee = Employees(**body)

    db.session.add(employee)
    db.session.commit()
    return {"message": "New employee added successfully"}


@app.route('/api/auth/login', methods=["POST"])
def log_in():
    print(f'request:{request.json}')
    username, password = request.json['username'], request.json['password']

    admin_account = Admins.query.filter_by(username=username).first()
    
    #print(f'username:{username} | password:{password} | admin_account:{admin_account}')
    if admin_account is None:
        # Username doesn't exist. But don't inform the client with that as
        # they can use it to bruteforce valid usernames
        return exceptions.Unauthorized(
            description="Incorrect username/password combination")
    # Checking if such hash can be generated from that password
    is_password_correct = hashing_service.check_bcrypt(
        password.encode("utf8"), admin_account.password_hash.encode("utf8"))

    if not is_password_correct:
        return exceptions.Unauthorized(
            description="Incorrect username/password combination")
    
    token_payload = {"username": username}
    token = jwt_service.generate(token_payload)
    if token is None:
        return exceptions.InternalServerError(description="Login failed")
    return {"token": token}


@app.route('/api/auth/sing_up', methods=["POST"])
def sign_up():
    username, password = request.json['username'], request.json['password']
    if request.headers.get("sing_up_key") != "sing_up_key":
        exceptions.Unauthorized(description="Incorrect Key")


    password_hash = hashing_service.hash_bcrypt(
        password.encode("utf-8")).decode("utf-8")
    admin = Admins(username=username, password_hash=password_hash)
    db.session.add(admin)
    db.session.commit()
    return {"message": "Admin account created successfully"}


@app.route('/api/auth/is_logged_in')
def is_logged_in():
    # If this controller is reached this means the
    # Auth middleware recognizes the passed token
    return {"message": "Token is valid"}


app.run()
