from models import Account
from flask import Flask, render_template, redirect, url_for, request, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://scx:y2K.scx@scx/scxcp'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


class AccountSchema(ma.Schema):
    class Meta:
        fields = ('name','address','email')

account_schema = AccountSchema()
accounts_schema = AccountSchema(many=True)


@app.route('/account', methods=['GET', 'POST'])
def get_account():
    if request.method == 'POST':
        name = request.json['name']
        address = request.json['address']
        email = request.json['email']

        nueva_account = Account(name, address, email)
        db.session.add(nueva_account)
        db.session.commit()

        return account_schema.jsonify(nueva_account)
    
    elif request.method == 'GET':
        all_accounts = Account.query.all()
        result = accounts_schema.dump(all_accounts)

        return jsonify(result)


@app.route('/prueba', methods=['POST'])
def create_prueba():
    name = request.json['name']
    address = request.json['address']
    email = request.json['email']

    nueva_prueba = Prueba(name, address, email)
    db.session.add(nueva_prueba)
    db.session.commit()

    return prueba_schema.jsonify(nueva_prueba)


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


# Run application
if __name__ == "__main__":
    app.run(debug=True)
