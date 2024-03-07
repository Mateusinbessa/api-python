#Libs
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required
from flask import make_response, jsonify, request, Flask

#Self-imports
from config import JWT_SECRET_KEY
from functions import connectDB
from extensions import jwt

db = connectDB()

#API Configs
app = Flask(__name__)
app.json.sort_keys = False
app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY

jwt.init_app(app)

#Routes
@app.route('/carros', methods=['GET'])
@jwt_required()
def get_carros():
    #TODO: Virar função dentro do MODEL
    try:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM carros')
        meus_carros = cursor.fetchall()
    except Exception as e:
        print(f'Error in getting cars: {e}')
    
    carros = []
    #TODO: Dá pra fazer virar função
    for carro in meus_carros:
        carros.append({
            'id': carro[0],
            'marca': carro[1],
            'modelo': carro[2],
            'ano': carro[3]
        })

    return make_response(jsonify(
        message='Lista de carros',
        carros=carros       
    ))

@app.route('/carros', methods=['POST'])
@jwt_required
def create_carro():
    carro = request.json
    
    #TODO: Virar função dentro de um MODEL
    try:
        cursor = db.cursor()
        query = f"INSERT INTO carros (marca, modelo, ano) VALUES ('{carro['marca']}', '{carro['modelo']}', {carro['ano']})"
        cursor.execute(query)
        db.commit()
    except Exception as e:
        print(f'Erro in posting car: {e}')
        return

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