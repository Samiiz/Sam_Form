from app.models import User
from config import db
from flask import request, jsonify

def create_user():
    data = request.get_json()
    user=User(
        name=data['name'],
        age=data['age'],
        gender=data['gender'],
        email=data['email']
    )

    db.session.add(user)
    db.session.commit()
    return user, jsonify({"message": f"{data['name']}User created successfully"}), 201

def get_user():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    return jsonify(user.to_dict())

def get_all_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

