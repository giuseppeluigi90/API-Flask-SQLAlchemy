from flask_sqlalchemy import SQLAlchemy, Column, Integer, String

class Prueba(db.Model):
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

# db.create_all()