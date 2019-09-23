# pymongo-project

El objetivo del proyecto es establecer la mejor localización para una empresa de videojuegos. La decisión depende de varias condiciones planteadas por los trabajadores, como el deseo de los diseñadores de estar junto a otras empresas del mismo sector, que las compañías más próximas hayan sido capaces de ganar más de un millón o de la exigencia impuesta por el CEO para tener restaurantes veganos cerca.

## Pasos dados:

### Obtención y limpieza de los datos

Los datos se obtienen a través de la importación de una base de datos en MongoDB sobre compañías tecnológicas en formato json. Tras la conexión con la base de datos y su respectiva colección a través de PyMongo, planteo una primera query para filtrar las compañías de aquellos sectores similares al de la empresa planteada. El filtro también se establece por un mínimo de trabajadores y por el hecho de que las empresas no hayan quebrado.

Tras esta primera query, limpio otros datos (valores nulos en la longitud y latitud de las empresas, por ejemplo) con la aplicación de funciones en Pandas.

Por último, creo un geopoint para volver a exportar los datos a MongoDB.

### Análisis de los datos

Una vez creado un geoindice en los documentos exportados a MongoDB, vuelvo a importarlos a un jupyter Notebook


### Conclusión