from flask import Flask, render_template, redirect, url_for, request, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://scx:y2K.scx@localhost/scxcp'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

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

class PruebaSchema(ma.Schema):
    class Meta:
        fields = ('id','name','address','email')

prueba_schema = PruebaSchema()
pruebas_schema = PruebaSchema(many=True)

# Prueba
@app.route('/prueba', methods=['POST'])
def create_prueba():
    name = request.json['name']
    address = request.json['address']
    email = request.json['email']

    nueva_prueba = Prueba(name, address, email)
    db.session.add(nueva_prueba)
    db.session.commit()

    return prueba_schema.jsonify(nueva_prueba)

@app.route('/prueba', methods=['GET'])
def get_pruebas():
    all_pruebas = Prueba.query.all()
    result = pruebas_schema.dump(all_pruebas)

    return jsonify(result)

@app.route('/prueba/<id>', methods=['GET'])
def get_prueba(id):
    prueba = Prueba.query.get(id)
    return prueba_schema.jsonify(prueba)

@app.route('/prueba/<id>', methods=['PUT'])
def update_prueba(id):
    prueba = Prueba.query.get(id)

    name = request.json['name']
    address = request.json['address']
    email = request.json['email']

    prueba.name = name
    prueba.address = address
    prueba.email = email

    db.session.commit()
    return prueba_schema.jsonify(prueba)

# Dashboard
@app.route('/dashboard')
def dashboard():
    return render_template('layout.html')

@app.route('/ping')
def index():
    return "<h1 style='color: red'> <a href='/dashboard'>  Pong... </a> </h1>"

if __name__ == "__main__":
    app.run(debug=True)
