from pymongo import MongoClient
from datetime import datetime, timedelta

# Conexión a tu clúster (ajusta tu contraseña real)
uri = "mongodb+srv://cam22155:sOvqRirmsLKMiWg5@lab6.qrfyn.mongodb.net/?retryWrites=true&w=majority&appName=lab6"
client = MongoClient(uri)
db = client["mi_laboratorio"]
usuarios = db["usuarios"]

# a. Usuarios activos con más de 500 puntos
print("a. Usuarios activos con más de 500 puntos:")
resultado_a = usuarios.find({
    "archivo": True,  # Asumiendo que 'archivo' significa 'activo'
    "puntos": {"$gt": 500}
})
for doc in resultado_a.limit(5):  # Muestra los primeros 5
    print(doc["nombre"], doc["puntos"])

# b. Usuarios que han comprado el producto "Producto 1" en la última semana
print("\nb. Usuarios que compraron 'Producto 1' en la última semana:")
hace_una_semana = datetime.now() - timedelta(days=7)
resultado_b = usuarios.find({
    "historial_compras": {
        "$elemMatch": {
            "producto": "Producto 1",
            "fecha": {"$gte": hace_una_semana}
        }
    }
})
for doc in resultado_b.limit(5):
    print(doc["nombre"])

# c. Usuarios con etiqueta "tag2" y más de 100 visitas
print("\nc. Usuarios con 'tag2' y más de 100 visitas:")
resultado_c = usuarios.find({
    "tags": "tag2",
    "visitas": {"$gt": 100}
})
for doc in resultado_c.limit(5):
    print(doc["nombre"], doc["visitas"])

# d. Usuarios con color "azul" y entre 1000 y 2000 amigos
print("\nd. Usuarios con preferencias de color 'azul' y 1000-2000 amigos:")
resultado_d = usuarios.find({
    "preferencias.color": "azul",
    "$expr": {
        "$and": [
            {"$gte": [{"$size": "$amigos"}, 1000]},
            {"$lte": [{"$size": "$amigos"}, 2000]}
        ]
    }
})
for doc in resultado_d.limit(5):
    print(doc["nombre"], "n. amigos:", len(doc["amigos"]))
