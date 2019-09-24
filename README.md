# pymongo-project

El objetivo del proyecto es encontrar la mejor localización para una empresa de videojuegos. La decisión depende de varias condiciones planteadas por los trabajadores, como el deseo de los diseñadores de estar junto a otras empresas del mismo sector, que las compañías más próximas hayan sido capaces de ganar más de un millón o de la exigencia impuesta por el CEO para tener restaurantes veganos cerca.

## Pasos dados:

### Obtención y limpieza de los datos

Los datos se obtienen a través de la importación de una base de datos en MongoDB sobre compañías tecnológicas en formato json. Tras la conexión con la base de datos y su respectiva colección a través de PyMongo, planteo una primera query para filtrar las compañías de aquellos sectores similares al de la empresa planteada. El filtro también se establece por un mínimo de trabajadores y por el hecho de que las empresas no hayan quebrado.

Tras esta primera query, limpio otros datos (valores nulos en la longitud y latitud de las empresas, por ejemplo) con la aplicación de funciones en Pandas. Por último, creo un geopoint para volver a exportar los datos a MongoDB.

### Análisis de los datos

Una vez creado un geoindice en los documentos exportados a MongoDB, vuelvo a importarlos a un Jupyter Notebook. Con la creación de varias funciones con el operador $near obtengo más datos como el número total de compañías situadas a un kilómetro a la redonda de una dada, así como el dinero total acumulado o el número de trabajadores en esa misma área. Además, extraigo datos de la api de Zomato para gelocalizar restaurants veganos, cafeterías y bares próximos a esas empresas. 


### Conclusión

Para hallar la localización final de la empresa planteada tomo como referencia la ciudad de San Francisco. Según los datos obtenidos, concentra el mayor número de empresas de videojuegos y de otros sectores tecnológicos. A su vez, tomo como refrencia la compañía instalada en la ciudad californiana que más dinero ha obtenido y geolocalizo con sus coordenadas los restaurantes veganos, bares y cafeterías en un radio de un kilómetro.


<img scr:"./output/empresa.png>
<img scr:"./output/mapa.png">



Por tanto, las coordenadas elegidas para lo localización de la empresa son: 


### Próximos pasos

El mismo análisis hecho para San Francisco se podría hacer en Nueva York y Seattle. Las otras dos ciudades, según los datos obtenidos, que concentran un número de empresas suficientes. También se podrían obtener más datos de otras Apis con el objetivo de cumplir más requsitios planteados por los trabajadores (aeropuertos y colegios próximos, por ejemplo).