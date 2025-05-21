# API Rest MongoDB
Ejemplo de una API REST con MongoDB + Docker

# Clonar repositorio
## Opción 1 (Manual)
 1.- Hacer click en el botón __CODE <>__  
 2.- Hacer click en el botón __Download ZIP__   
<img width="407" alt="image" src="https://github.com/user-attachments/assets/ec0e5f1e-3254-4d2b-9b69-f19c88e9c205" />

## Opción 2 (Terminal) 
Ejecutar  
```
  git clone https://github.com/mevangelista-alvarado/api_rest_mongo.git
```

# Deploy in Render
## Deploy in Web
<img width="1377" alt="image" src="https://github.com/user-attachments/assets/7f360c19-7bb2-46c9-997f-9ccd7bd3741d" />
<img width="1364" alt="image" src="https://github.com/user-attachments/assets/176ac4b3-b36b-4dff-b904-2ce429e152c4" />
<img width="1381" alt="image" src="https://github.com/user-attachments/assets/7de382af-611c-4c0e-abef-e39449a65e87" />
Agregamos la variable de entorno **MONGO_URI** con la siguente estructra  

```
mongodb+srv://{{USER}}:{{PASSWORD}}@{{CLUSTERNAME}}.3njsr11.mongodb.net/{{DATABASE}}?retryWrites=true&w=majorityt&appName={{CLUSTER_APPNAME}}
```  

recomendamos al lector copiar y pegar la uri desde MongoAtlas.  
<img width="1371" alt="image" src="https://github.com/user-attachments/assets/92c9aef6-7d00-4994-80b7-c5dbdf2bec0c" />  

Por último, damos **Deploy Web Service**.

## Último paso
Correr el siguiente [Google Colab](https://colab.research.google.com/drive/1NOx8aqK2snQugfmRWArnHylOPHmB0wMF?usp=sharing)

# Entorno Local (Docker)
## Primera Vez
1.- Crear un archivo `.env` (Tome como referencia el archivo `.env_example` y no olvide actulizar los valores)  

2a.- Abrir una terminal (en la carpeta donde este el archivo `docker-compose.yml`)   
3a.- Ejecutar  
```
  docker-compose up --build
```  

2b.- Abrir una terminal nueva (en la carpeta donde este el archivo `docker-compose.yml` & `init_db.py`)
3b.- Ejecutar  
```
  docker-compose exec web python init_db.py
```

4.- Visitar en su navegador [http://localhost:5050/](http://localhost:5050/)  

## Si NO es la primera vez
1.- Abrir una terminal (en la carpeta donde este el archivo `docker-compose.yml`)   
2.- Ejecutar
```
  docker-compose up
```
3.- Visitar en su navegador [http://localhost:5050/](http://localhost:5050/)


# Miscelania 
## Probar PostgreSQL
Para probar MongoDB, vaya a Docker Desktop y seleccione (dar click) el servicio de mongo (db-1) 

<img width="331" alt="image" src="https://github.com/user-attachments/assets/3ec33659-8b69-47a0-8dba-86dffa9c5d6f" />


Después damos click en terminal  

<img width="377" alt="image" src="https://github.com/user-attachments/assets/c2062f13-a0d4-4098-9207-dd959b9f6c8c" />

Ejecute 
```
mongosh "mongodb://mongo:mongo@localhost:27017/mydb?authSource=admin"
```
<img width="1167" alt="image" src="https://github.com/user-attachments/assets/bf63eaf4-2e4b-47d3-bf1d-bf0438962ad8" />

Y ya estará dentro de la terminal de MongoDB

### Consultado el contenido de una base de datos

Para listar bases de datos, ejecute
```
show dbs 
```
<img width="175" alt="image" src="https://github.com/user-attachments/assets/b73e99c1-942b-40b6-b5e2-80ea2fc36f5c" />


Para conectarte a la base de datos `mydb`
```
use mydb
```
<img width="148" alt="image" src="https://github.com/user-attachments/assets/6cfc1874-d84e-4d02-be9d-7905c7e26c8d" />


Para listar las colecciones de la base de datos `mydb`
```
show collections    
```
<img width="204" alt="image" src="https://github.com/user-attachments/assets/d342a16b-96b5-491a-99be-28735cbf7db6" />


Por último, para obtener todas los documentos de la colección `posts`
```
db.posts.find().pretty()
```
<img width="421" alt="image" src="https://github.com/user-attachments/assets/b750fa46-f969-4496-9e05-9050c4fb95a0" />


