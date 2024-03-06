from flask import make_response, jsonify, request, Flask
from bd import carros

app = Flask(__name__)

@app.route('/carros', methods=['GET'])
def get_carros():
    return make_response(jsonify(
        message='Lista de carros',
        carros=carros
    ))

@app.route('/carros', methods=['POST'])
def create_carro():
    carro = request.json
    print(carro)
    return make_response(jsonify(
        message='Carro cadastrado com sucesso',
        carro=carro
    ))

#Rodar server
app.run()