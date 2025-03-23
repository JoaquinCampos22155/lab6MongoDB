from pymongo import MongoClient
from datetime import datetime, timedelta
import pprint

# Conexión a MongoDB Atlas
uri = "mongodb+srv://cam22155:sOvqRirmsLKMiWg5@lab6.qrfyn.mongodb.net/?retryWrites=true&w=majority&appName=lab6"
client = MongoClient(uri)
db = client["mi_laboratorio"]
usuarios = db["usuarios"]

pp = pprint.PrettyPrinter(indent=2)

# Consulta a: Usuarios activos con más de 500 puntos
print("\n📊 Evaluación A: Usuarios activos con más de 500 puntos")
query_a = {
    "archivo": True,
    "puntos": {"$gt": 500}
}
stats_a = usuarios.find(query_a).explain("executionStats")
pp.pprint(stats_a["executionStats"])

# Consulta b: Usuarios que compraron 'Producto 1' en la última semana
print("\n📊 Evaluación B: Usuarios que compraron 'Producto 1' en la última semana")
hace_una_semana = datetime.now() - timedelta(days=7)
query_b = {
    "historial_compras": {
        "$elemMatch": {
            "producto": "Producto 1",
            "fecha": {"$gte": hace_una_semana}
        }
    }
}
stats_b = usuarios.find(query_b).explain("executionStats")
pp.pprint(stats_b["executionStats"])

# Consulta c: Usuarios con 'tag2' y más de 100 visitas
print("\n📊 Evaluación C: Usuarios con 'tag2' y más de 100 visitas")
query_c = {
    "tags": "tag2",
    "visitas": {"$gt": 100}
}
stats_c = usuarios.find(query_c).explain("executionStats")
pp.pprint(stats_c["executionStats"])

# Consulta d: Preferencias de color 'azul' y 1000-2000 amigos
print("\n📊 Evaluación D: Usuarios con color 'azul' y entre 1000 y 2000 amigos")
query_d = {
    "preferencias.color": "azul",
    "$expr": {
        "$and": [
            {"$gte": [{"$size": "$amigos"}, 1000]},
            {"$lte": [{"$size": "$amigos"}, 2000]}
        ]
    }
}
stats_d = usuarios.find(query_d).explain("executionStats")
pp.pprint(stats_d["executionStats"])
