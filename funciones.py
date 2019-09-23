def tes():
    print("AAAAA")
    
def get_divisas(col, divisas):

    # Función para obtener las diferentes monedas
    
    for divisa, nombre in divisas.items():
        if divisa in col:
            return nombre
        else:
            return "unknown"


def get_values(value, divisas, valores):

    # Función para obtener los diferentes valores de las monedas

    try:
        for k in divisas.keys():
            value = value.replace(k, "")
        
        for item, number in valores.items():
            if item in value:
                value = value.replace(item, "")
                return float(value) * number
        return float(value)

    except:
        return value



def get_ciudades(col, ciudades):

    # Función para ordenar la columna de las ciudades y filtrar luego solo las que me interesan

    if col not in ciudades:
        return "other"
    else:
        return col
        

def geopoint(longitude, latitude):

    # Función para obtener el geopoint

    return {"type":"Point", "coordinates": [longitude, latitude]}

