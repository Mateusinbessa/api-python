# @Description: Formatar os carros que vem do DB de Tupla para dincionário.
def formatting(meus_carros):
    carros = []
    for carro in meus_carros:
        carros.append({
            'id': carro[0],
            'marca': carro[1],
            'modelo': carro[2],
            'ano': carro[3]
        })
    return carros