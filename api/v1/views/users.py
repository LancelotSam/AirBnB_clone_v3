#!usr/bin/python3
"""users"""

from flask import jsonify, abort, request
from models import storage
from api.v1.views import app_views
from models.user import User
from datetime import datetime
import uuid

@app_views.route('/users/', methods=['GET'], strict_slashes=FALSE)
def list_users():
    """Retrieves the list of all users"""
    list_users = [obj.to_dict() for obj in storage.all("User").values()]
    return jsonify(list_users)

@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=FALSE)
def userId(user_id):
    """gets user id"""
    all_users = storage.all("User").values()
    user_obj = [obj.to_dict() for obj in all_users if obj.id == user_id]
    if user_obj == []:
        abort(404)
    return jsonify(user_obj[0])

@app_views.route('/users/<user_id>', methods=['POST'], strict_slashes=FALSE)
def create_user():
    """creates a user object"""
    if not request.get_json():
        abort(400, 'Not a JSON')
    if 'email' not in request.get_json():
        abort(400, 'Missing name')
    if 'password' not in request.get_json():
        abort(400, 'Missing name')
    
    users = []
    new_user = User(email=request.json['email'],
                    password=request.json['password'])
    storage.new(new_user)
    storage.save()
    users.append(new_user.to_dict())
    return jsonify(users[0]), 201

@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=FALSE)
def delete_user(user_id):
    """deletes a user object"""
    all_users = storage.all("User").values()
    user_obj = [obj.to_dict() for obj in all_users if obj.id == user_id]
    if user_obj == []:
        abort(404)
    
    user_obj.remove(user_obj[0])
    for obj in all_users:
        if obj.id == user_id:
            storage.delete(obj)
            storage.save()
    return jsonify({}), 200

@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=FALSE)
def update_state():
    """updates a state object"""
    all_users = storage.all("User").values()
    user_obj = [obj.to_dict() for obj in all_users if obj.id == user_id]
    if user_obj == []:
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')
    try:
        user_obj[0]['first_name'] = request.json['first_name']
    except:
        pass
    try:
        user_obj[0]['last_name'] = request.json['last_name']
    except:
        pass
    for obj in all_users:
        if obj.id == user_id:
            try:
                if request.json['first_name'] is not None:
                    obj.first_name = request.json['first_name']
            except:
                pass
            try:
                if request.json['last_name'] is not None:
                    obj.last_name = request.json['last_name']
            except:
                pass
    storage.save()
    return jsonify(user_obj[0]), 200
