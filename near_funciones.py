def getCompaniesNear(db, geopoint, max_meters=1000):

    # Función para obtener el número de empresas situadas a un km a la redonda del punto seleccionado

    return len(list(db.find({
        "geo": {
            "$near": {
                "$geometry": geopoint,
                "$maxDistance": max_meters
            }
        }
    })))


def getEmployees(db, geopoint, max_meters=1000):

    # Función para obtener el número de empleados que trabajan en las diferentes empresas situadas a un km a la redonda

    info = list(db.find({
        "geo": {
            "$near": {
                "$geometry": geopoint,
                "$maxDistance": max_meters
            }
        }
    }))

    total = 0
    for e in info:
        total += e["number_of_employees"]
    return total


def getMoney(db, geopoint, max_meters=1000):

    # Función para calcular el dinero total de las empresas situadas a un km a la redonda

    info = list(db.find({
        "geo": {
            "$near": {
                "$geometry": geopoint,
                "$maxDistance": max_meters
            }
        }
    }))

    total = 0
    for e in info:
        total += e["total_amount_raised"]
    
    return total

'''

    def getMoney(geopoint, max_meters=1000):
    info = list(db.clean_companies.find({
        "geo": {
            "$near": {
                "$geometry": geopoint,
                "$maxDistance": max_meters
            }
        }
    }))
    
    total = 0
    for e in info:
        total += e["total_amount_raised"]
    return total

'''