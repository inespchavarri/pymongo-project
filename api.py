# Api Zomato

def getVeganRestaurants(lat, lon):

    # Función para obtener los restaurantes vegetarianos situados a un km a la redonda de un punto seleccionado

    headers = {
        "user-key": "{}".format(zomato_key)
    }
    url = "https://developers.zomato.com/api/v2.1/search?lat={}&lon={}&radius=1000&cuisines=308".format(lat, lon)
    response = requests.get(url, headers=headers)
    response = response.json()
    return response



