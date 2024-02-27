#!usr/bin/python3
"""places reviews"""

from flask import jsonify, abort, request
from models import storage
from models.place import Place
from models.review import Review
from api.v1.views import app_views
from datetime import datetime
import uuid

@app_views.route('/places/<place_id>/reviews', methods=['GET'], strict_slashes=FALSE)
def get_places_reviews():
    """Retrieves the list of all reviews"""
    all_places = storage.all("Place").values()
    places_obj = [obj.to_dict() for obj in all_places if obj.id == place_id]

    if place_obj == []:
        abort(404)
    list_reviews = [obj.to_dict() for obj in storage.all("Review").values()
                    if place_id == obj.place_id]
    return jsonify(list_reviews)

@app_views.route('/reviews/<review_id>', methods=['GET'], strict_slashes=FALSE)
def get_review(review_id):
    '''Retrieves a Review object '''
    all_reviews = storage.all("Review").values()
    rev_object = [obj.to_dict() for obj in all_reviews if obj.id == review_id]
    if rev_object == []:
        abort(404)
    return jsonify(rev_obj[0])

@app_views.route('/places/<place_id>/reviews', methods=['POST']), strict_slashes=FALSE
def create_review(place_id):
    '''Creates a Review'''
    if not request.get_json():
        abort(400, 'Not a JSON')
    if 'user_id' not in request.get_json():
        abort(400, 'Missing user_id')
    user_id = request.json['user_id']
    if 'text' not in request.get_json():
        abort(400, 'Missing text')
    all_places = storage.all("Place").values()
    place_obj = [obj.to_dict() for obj in all_places if obj.id == place_id]
    if place_obj == []:
        abort(404)
    all_users = storage.all("User").values()
    user_obj = [obj.to_dict() for obj in all_users if obj.id == user_id]
    if user_obj == []:
        abort(404)
    reviews = []
    new_review = Review(text=request.json['text'], place_id=place_id,
                        user_id=user_id)
    storage.new(new_review)
    storage.save()
    reviews.append(new_review.to_dict())
    return jsonify(reviews[0]), 201


@app_views.route('/reviews/<review_id>', methods=['DELETE'], strict_slashes=FALSE)
def delete_review():
    """deletes a review object"""
    all_reviews = storage.all("Review").values()
    rev_object = [obj.to_dict() for obj in all_reviews if obj.id == review_id]
    if rev_object == []:
        abort(404)
    rev_object.remove(rev_obj[0])
    for obj in all_reviews:
        if obj.id == review_id:
            storage.delete(obj)
            storage.save()
    return jsonify({}), 200

@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=FALSE)
def update_review(review_id):
    """updates a review object"""

    all_reviews = storage.all("Review").values()
    rev_object = [obj.to_dict() for obj in all_reviews if obj.id == review_id]
    if rev_obj == []:
        abort(404)

    if not request.get_json():
        abort(400, {'Not a JSON'})

    if 'text' in request.get_json():
        rev_object[0]['text'] == requests.json['text']
        for obj in all_reviews:
            if obj.id == review_id:
                obj.text = request.json['text']
        storage.save()
    return jsonify(rev_object[0]), 200
