from flask import Flask

app = Flask(__name__)
#Comandos docker
# Construye la imagen de Docker
#docker build -t my-flask-app .

# Ejecuta la imagen en un contenedor
#docker run -p 5001:5000 my-flask-app

#Borra todas las imagenes, contenedores y volumenes de docker
#docker system prune -a

@app.route('/returnRedis/<int:id>')
def index(id):
    if 4 <= id <= 275:
        return "redis1 hola"
    elif 276 <= id <= 581:
        return "redis2"
    else:
        return "redis3"
    
    #verificar si esta en cache
        #si esta en cache retornar informacion
        #else preguntar a la api la informacion y luego almacenar en cache y responder con informacion https://restcountries.com/v3.1/alpha/id

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

