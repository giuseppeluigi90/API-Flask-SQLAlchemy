from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

DB = SQLAlchemy()

class Prueba(DB.Model):
    id = Column(Integer, primary_key = True)
    name = Column(String)
    address = Column(String)
    email = Column(String)

    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.name

    Pru = Prueba()

# db.create_all()