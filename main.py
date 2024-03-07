#Libs
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, JWTManager
from flask import make_response, jsonify, request, Flask

#Self-imports
from models.carro import getAll, create
from controllers.carro import formatting
from config import JWT_SECRET_KEY

#API Configs
app = Flask(__name__)
app.json.sort_keys = False
app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
jwt = JWTManager()
jwt.init_app(app)

#Routes
@app.route('/carros', methods=['GET'])
@jwt_required()
def get_carros():
    meus_carros = getAll()
    carros_formatados = formatting(meus_carros)
    return make_response(jsonify(
        message='Lista de carros',
        carros=carros_formatados       
    ))

@app.route('/carros', methods=['POST'])
@jwt_required()
def create_carro():
    carro = request.json
    create(carro)
    
    return make_response(jsonify(
        message='Carro cadastrado com sucesso',
        carro=carro
    ))

@app.route('/login', methods=['POST'])
def login():
    email = request.json.get("email")
    password = request.json.get("password")
    
    access_token = create_access_token(identity=1)
    refresh_token = create_refresh_token(identity=1)
    
    return make_response(jsonify(
        access_token = access_token,
        refresh_token = refresh_token
    ))

app.run()