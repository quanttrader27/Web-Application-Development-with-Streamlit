from .Base import db


class Admins(db.Model):
    __tablename__ = 'admins'
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String)
    password_hash = db.Column(db.String, default=True)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "password_hash": self.password_hash
        }
