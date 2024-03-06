from flask import make_response, jsonify, request, Flask
import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='test'
)
app = Flask(__name__)
app.json.sort_keys = False

@app.route('/carros', methods=['GET'])
def get_carros():
    try:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM carros')
        meus_carros = cursor.fetchall()
    except Exception as e:
        print(f'Error in getting cars: {e}')
    
    carros = []
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
def create_carro():
    carro = request.json
    
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

app.run()