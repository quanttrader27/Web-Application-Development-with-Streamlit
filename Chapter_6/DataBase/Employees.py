from sqlalchemy import Column, Integer, String
from .Base import db


class Employees(db.Model):
    __tablename__ = 'persons'
    id = db.Column(Integer, primary_key=True)

    name = db.Column(String)
    date_of_birth = db.Column(String, default=True)
    paygrade_id = db.Column(Integer, unique=True, index=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "date_of_birth": self.date_of_birth,
            "paygrade_id": self.paygrade_id
        }
