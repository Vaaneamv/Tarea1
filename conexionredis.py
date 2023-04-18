import redis
import requests

# Cree conexiones a los tres servidores Redis
redis_1 = redis.Redis(host='localhost', port=6379, db=0)
redis_2 = redis.Redis(host='localhost', port=6380, db=0)
redis_3 = redis.Redis(host='localhost', port=6381, db=0)
