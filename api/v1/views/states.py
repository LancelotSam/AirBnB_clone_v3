#!/usr/bin/python3

"""states"""

from flask import jsonify, abort, request
from models import storage
from models.state import State
from api.v1.views import app_views
from datetime import datetime
import uuid

@app_views.route('/states', methods=['GET'], strict_slashes=FALSE)
def get_states():
    """Retrieves the list of all states"""
    objects = storage.all('State')
    liste = []
    for state in objects.values():
        liste.append(state.to.dict())
    return jsonify(liste)

@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=FALSE)
def statesId():
    """gets states id"""
    objects = storage.get('State', 'state_id')
    if objects is None:
        abort(404)
    return jsonify(objects.to.dict()), 'OK'

@app_views.route('/states/<state_id>', methods=['DELETE'], strict_slashes=FALSE)
def delete_state():
    """deletes a state object"""
    objects = storage.get('State', 'state_id')
    if objects is None:
        abort(404)
    storage.delete(stateObject)
    storage.save()
    return jsonify({}), "200"

@app_views.route('/states', methods=['POST'], strict_slashes=FALSE)
def create_state():
    """posts a state object"""
    response = request.get_json()

    if response id None:
        abort(404, {'Not a JSON'})

    if "name" not in response:
        abort(400, {'Missing name'})

    stateObject = State(name=response['name'])
    storage.new(stateObject)
    storage.save()
    return jsonify(stateObject.to.dict()), "201"

@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=FALSE)
def update_state():
    """updates a state object"""
    response = request.get_json()

    if response id None:
        abort(400, {'Not a JSON'})

    stateObject = storage.get('State', 'state_id')
    
    if stateObject is None:
        abort(404)

    ignorekeys = ['id', 'created_at', 'updated_at']
    for key in response.items():
        if key not in ignoreKeys:
            setattr(stateObject, key)
    storage.save()
    return jsonify(stateObject.to.dict()), "200"
