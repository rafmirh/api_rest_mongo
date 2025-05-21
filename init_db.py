from app import app
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

MONGO_URI = os.environ.get("MONGO_URI", "")
client = MongoClient(MONGO_URI)
# Obtiene la base de datos del URI
db = client.get_default_database()
# Colección "posts"  
posts_collection = db['posts']

# Insertar datos iniciales si la colección está vacía
if posts_collection.count_documents({}) == 0:
    posts_iniciales = [
        {'usuario': 'ana', 'contenido': 'Hola, este es mi primer post'},
        {'usuario': 'carlos', 'contenido': 'Buenos días a todos'},
        {'usuario': 'ana', 'contenido': 'Estoy aprendiendo Flask'},
        {'usuario': 'maria', 'contenido': 'Hoy fue un gran día'},
        {'usuario': 'luis', 'contenido': '¿Alguien recomienda libros de Python?'},
        {'usuario': 'julia', 'contenido': 'Feliz lunes a todos'},
        {'usuario': 'carlos', 'contenido': 'Me encanta programar en Flask'},
        {'usuario': 'maria', 'contenido': 'Estoy probando esta API REST'},
        {'usuario': 'ana', 'contenido': '¿Quién quiere colaborar en un proyecto?'},
        {'usuario': 'luis', 'contenido': 'Estoy creando un bot en Telegram'},
    ]

    posts_collection.insert_many(posts_iniciales)
    print("Datos iniciales insertados")
else:
    print("Ya existen datos, no se insertó nada.")
