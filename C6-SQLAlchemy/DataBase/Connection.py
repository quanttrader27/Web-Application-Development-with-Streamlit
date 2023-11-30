from flask_sqlalchemy import SQLAlchemy


def Connection(app,conn):
    
    app.config['SQLALCHEMY_DATABASE_URI'] = conn
    db = SQLAlchemy(app)

    return db


