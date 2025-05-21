import os
from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)

# Conexión manual con pymongo
MONGO_URI = os.environ.get("MONGO_URI", "")
client = MongoClient(MONGO_URI)
# Obtiene la base de datos del URI
db = client.get_default_database()
# Colección "posts"  
posts_collection = db['posts'] 

# Helpers
def post_to_json(post):
    return {
        'id': str(post['_id']),
        'usuario': post['usuario'],
        'contenido': post['contenido']
    }

# Rutas
@app.route('/posts', methods=['GET'])
def obtener_todos_los_posts():
    posts = posts_collection.find()
    return jsonify([post_to_json(p) for p in posts])

@app.route('/posts/<usuario>', methods=['GET'])
def obtener_posts_por_usuario(usuario):
    posts = posts_collection.find({'usuario': usuario})
    return jsonify([post_to_json(p) for p in posts])

@app.route('/posts', methods=['POST'])
def crear_post():
    datos = request.json
    nuevo_post = {
        'usuario': datos['usuario'],
        'contenido': datos['contenido']
    }
    resultado = posts_collection.insert_one(nuevo_post)
    post_insertado = posts_collection.find_one({'_id': resultado.inserted_id})

    return jsonify(post_to_json(post_insertado)), 201


@app.route('/posts/<post_id>', methods=['PATCH'])
def actualizar_post(post_id):
    datos = request.json
    resultado = posts_collection.update_one(
        {'_id': ObjectId(post_id)},
        {'$set': {'contenido': datos['contenido']}}
    )
    if resultado.matched_count == 0:
        return jsonify({'error': 'Post no encontrado'}), 404

    post_actualizado = posts_collection.find_one({'_id': ObjectId(post_id)})
    return jsonify(post_to_json(post_actualizado))

@app.route('/posts/<post_id>', methods=['DELETE'])
def eliminar_post(post_id):
    post = posts_collection.find_one({'_id': ObjectId(post_id)})
    print(post)
    if not post:
        return jsonify({'error': 'Post no encontrado'}), 404

    posts_collection.delete_one({'_id': ObjectId(post_id)})
    return jsonify(post_to_json(post))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
