# pymongo-project

El objetivo del proyecto es establecer la mejor localización para una empresa de videojuegos. La decisión depende de varias condiciones planteadas por los trabajadores, como el deseo de los diseñadores de estar junto a otras empresas del mismo sector, que las compañías más próximas hayan sido capaces de ganar más de un millón o de la exigencia impuesta por el CEO para tener restaurantes veganos cerca.

## Pasos dados:

### Obtención y limpieza de los datos

Los datos se obtienen a través de la importación de una base de datos en MongoDB sobre compañías tecnológicas en formato json. Tras la conexión con la base de datos y su respectiva colección a través de PyMongo, planteo una primera query para filtrar las compañías de aquellos sectores similares al de la empresa planteada. El filtro también se establece por un mínimo de trabajadores y por el hecho de que las empresas no hayan quebrado.

Tras esta primera query, limpio otros datos (valores nulos en la longitud y latitud de las empresas, por ejemplo) con la aplicación de funciones en Pandas. Por último, creo un geopoint para volver a exportar los datos a MongoDB.

### Análisis de los datos

Una vez creado un geoindice en los documentos exportados a MongoDB, vuelvo a importarlos a un jupyter Notebook. Con la creación de varias funciones con el operador $near obtengo más datos como el número total de compañías situadas a un kilometro a la redonda de una dada, así como el dinero total acumulado o el número de trabajadores en esa misma área. Además, extraigo datos de la api de Zomato para gelocalizar restaurants veganos próximos a esas empresas. 


### Conclusión


_id                                             5d83a90255488441b3fff58d
name                                                             Rupture
category_code                                                games_video
number_of_employees                                                   25
founded_year                                                         NaN
deadpooled_year                                                     None
description                                        Gaming Social Network
latitude                                                         37.7839
longitude                                                       -122.395
country                                                              USA
state                                                                 CA
city                                                       San Francisco
monedas                                          Dolares estadounidenses
total_amount_raised                                                3e+06
geo                    {'type': 'Point', 'coordinates': [-122.395234,...
num_companies                                                         27
num_employees                                                       2662
total_money            