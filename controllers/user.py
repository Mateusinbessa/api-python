#@Libs
from flask_jwt_extended import create_access_token, create_refresh_token
from flask import jsonify, make_response

def login():
    access_token = create_access_token(identity=1)
    refresh_token = create_refresh_token(identity=1)
    return make_response(jsonify(
        access_token = access_token,
        refresh_token = refresh_token
    ))