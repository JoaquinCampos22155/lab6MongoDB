from pymongo import MongoClient

# Conexión a tu clúster Atlas
uri = "mongodb+srv://cam22155:sOvqRirmsLKMiWg5@lab6.qrfyn.mongodb.net/?retryWrites=true&w=majority&appName=lab6"
client = MongoClient(uri)
db = client["mi_laboratorio"]
usuarios = db["usuarios"]

# a. Índice compuesto sobre archivo (activo) y puntos
print("🛠️ Creando índice sobre 'archivo' y 'puntos'...")
usuarios.create_index([("archivo", 1), ("puntos", 1)])

# b. Índice compuesto sobre 'historial_compras.producto' y 'historial_compras.fecha'
print("🛠️ Creando índice sobre 'historial_compras.producto' y 'historial_compras.fecha'...")
usuarios.create_index([("historial_compras.producto", 1), ("historial_compras.fecha", 1)])

# c. Índice compuesto sobre 'tags' y 'visitas'
print("🛠️ Creando índice sobre 'tags' y 'visitas'...")
usuarios.create_index([("tags", 1), ("visitas", 1)])

# d. Índice compuesto sobre 'preferencias.color' y 'amigos'
print("🛠️ Creando índice sobre 'preferencias.color' y 'amigos'...")
usuarios.create_index([("preferencias.color", 1), ("amigos", 1)])

print("✅ Todos los índices han sido creados.")
