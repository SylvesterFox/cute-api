import os
import random
from flask import Blueprint, jsonify, url_for

api = Blueprint('api', __name__)


@api.route('api/v1/fox', methods=['GET'])
def fox_image_json():
    _dir = os.listdir("project/static/img/fox")
    if _dir:
        name = random.choice(_dir)
        fox_image = [
            {
                'image': url_for('static', filename=f'img/fox/{name}', _external=True)
            }
        ]
    else:
        fox_image = [
            {
                'image': 'Not found image'
            }
        ]
    return jsonify(fox_image)

@api.route('api/v1/hug', methods=['GET'])
def hug_image_json():
    _dir = os.listdir("project/static/img/hug")
    if _dir:
        name = random.choice(_dir)
        hug_image = [
            {
                'image': url_for('static', filename=f'img/hug/{name}', _external=True)
            }
        ]
    else:
        hug_image = [{
            'image': 'Not found image'
        }]
    return jsonify(hug_image)

@api.route('api/v1/boop', methods=['GET'])
def boop_image_json():
    _dir = os.listdir("project/static/img/boop")
    if _dir:
        name = random.choice(_dir)
        boop_image = [
            {
                'image': url_for('static', filename=f'img/boop/{name}', _external=True)
            }
        ]
    else:
        boop_image = [{
            'image': 'Not found image'
        }]
    return jsonify(boop_image)

@api.route('api/v1/cuddle', methods=['GET'])
def cuddle_image_json():
    _dir = os.listdir("project/static/img/cuddle")
    if _dir:
        name = random.choice(_dir)
        cuddle_image = [
            {
                'image': url_for('static', filename=f'img/cuddle/{name}', _external=True)
            }
        ]
    else:
        cuddle_image = [{
            'image': 'Not found image'
        }]
    return jsonify(cuddle_image)


@api.route('api/v1/kiss', methods=['GET'])
def kiss_image_json():
    _dir = os.listdir("project/static/img/kiss")
    if _dir:
        name = random.choice(_dir)
        kiss_image = [
            {
                'image': url_for('static', filename=f'img/kiss/{name}', _external=True)
            }
        ]
    else:
        kiss_image = [{
            'image': 'Not found image'
        }]
    return jsonify(kiss_image)
