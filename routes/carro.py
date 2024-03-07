#@Libs
from flask import Blueprint
from flask_jwt_extended import jwt_required

#@Self-modules
from controllers.carro import getCars, createCar

carros_bp = Blueprint('carros_bp', __name__)

@carros_bp.route('/carros', methods=['GET'])
@jwt_required()
def getRoute():
    return getCars()

@carros_bp.route('/carros', methods=['POST'])
@jwt_required()
def createRoute():
    return createCar()

