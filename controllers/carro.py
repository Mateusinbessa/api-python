#@Libs
from flask import jsonify, make_response, request

#@Self-modules
from helpers.functions import formatting
from models.carro import getAll, create

def getCars():
    meus_carros = getAll()
    carros_formatados = formatting(meus_carros)
    return make_response(jsonify(
        message='Lista de carros',
        carros=carros_formatados       
    ))
    
def createCar():
    carro = request.json
    create(carro)
    
    return make_response(jsonify(
        message='Carro cadastrado com sucesso',
        carro=carro
    ))
    