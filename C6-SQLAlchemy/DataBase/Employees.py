from .Base import db


class Employees(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String)
    date_of_birth = db.Column(db.String, default=True)
    paygrade_id = db.Column(db.Integer, unique=True, index=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "date_of_birth": self.date_of_birth,
            "paygrade_id": self.paygrade_id
        }
