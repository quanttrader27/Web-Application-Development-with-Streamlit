from flask_sqlalchemy import SQLAlchemy

def Connection(conn):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = conn
    db = SQLAlchemy(app)

    return db


