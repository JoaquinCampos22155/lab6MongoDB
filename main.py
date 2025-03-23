from pymongo import MongoClient
from faker import Faker
from random import randint, choice, random
from datetime import datetime, timedelta
import random

# Conexión a MongoDB (ajusta URI si usas Atlas)
uri = "mongodb+srv://cam22155:sOvqRirmsLKMiWg5@lab6.qrfyn.mongodb.net/?retryWrites=true&w=majority&appName=lab6"
client = MongoClient(uri)
db = client["mi_laboratorio"]
usuarios = db["usuarios"]

# Faker en español
fake = Faker('es_MX')

def generar_usuario():
    historial = [{
        "producto": "Producto 1" if i % 3 == 0 else fake.word(),
        "fecha": fake.date_time_between(start_date='-2y', end_date='now')
    } for i in range(randint(1, 10))]

    tags = ["tag2"] if random.random() < 0.3 else [fake.word() for _ in range(randint(1, 4))]

    return {
        "nombre": fake.name(),
        "email": fake.email(),
        "fecha_registro": fake.date_time_between(start_date='-3y', end_date='now'),
        "puntos": randint(0, 1000),
        "historial_compras": historial,
        "dirección": {
            "calle": fake.street_name(),
            "ciudad": fake.city(),
            "codigo_postal": fake.postcode()
        },
        "tags": tags,
        "archivo": choice([True, False]),
        "notas": fake.sentence(),
        "visitas": randint(0, 10000),
        "amigos": [randint(1, 100000) for _ in range(randint(0, 1500))],
        "preferencias": {
            "color": choice(["azul", "verde", "rojo", "amarillo"]),
            "idioma": choice(["es", "en", "fr"]),
            "tema": choice(["claro", "oscuro"])
        }
    }

# Inserción masiva
usuarios.delete_many({})  # Opcional: limpia la colección antes
batch_size = 1000
for i in range(100):
    batch = [generar_usuario() for _ in range(batch_size)]
    usuarios.insert_many(batch)
    print(f"{(i+1)*batch_size} documentos insertados...")

print("✅ Inserción finalizada")
