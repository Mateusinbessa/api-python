from functions import connectDB
db = connectDB()

def getAll():
    try:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM carros')
        meus_carros = cursor.fetchall()
        return meus_carros
    except Exception as e:
        print(f'Error in getting cars: {e}')
 
def create(carro):
    try:
        cursor = db.cursor()
        query = f"INSERT INTO carros (marca, modelo, ano) VALUES ('{carro['marca']}', '{carro['modelo']}', {carro['ano']})"
        cursor.execute(query)
        db.commit()
    except Exception as e:
        print(f'Erro in posting car: {e}')
        return 