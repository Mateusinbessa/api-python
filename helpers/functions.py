# @Description: Format the cars list of tuple to list of dict
def formatting(meus_carros):
    cars = []
    for car in meus_carros:
        cars.append({
            'id': car[0],
            'marca': car[1],
            'modelo': car[2],
            'ano': car[3]
        })
    return cars