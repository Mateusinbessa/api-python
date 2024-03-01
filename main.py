from flask import make_response, jsonify, Flask
from bd import carros

app = Flask(__name__)

# Criando um rota para minha função get carros.
# Acima da declaração da função você marca ela com @app (decorator)
# Com esse decorator eu tou dizendo pro FLASK que essa função tá marcada como uma rota da nossa API.
@app.route('/carros', methods=['GET'])
def get_carros():
    return make_response(jsonify(carros))
     

#Rodar server
app.run()