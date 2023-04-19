from flask import Flask
import requests
import redis
from conexionredis import redis1, redis2, redis3  # Importar las variables redis1, redis2 y redis3 desde el archivo conexionredis

app = Flask(__name__)

@app.route('/returninformación/<string:id>')
def index(id):
    # Verificar si la consulta está en caché
    if 4 <= int(id) <= 275:
        if redis1.exists(id):
            return redis1.get(id)
    elif 276 <= int(id) <= 581:
        if redis2.exists(id):
            return redis2.get(id)
    elif 582 <= int(id) <= 1000:
        if redis3.exists(id):
            return redis3.get(id)
    else:
        # Si la consulta no está en caché, obtener la información de la API
        response = requests.get(f'https://restcountries.com/v3.1/alpha/{id}')
        data = response.json()

        # Almacenar la información en caché
        if 4 <= int(data['id']) <= 275:
            redis1.set(id, data)
        elif 276 <= int(data['id']) <= 581:
            redis2.set(id, data)
        else:
            redis3.set(id, data)

        return data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
