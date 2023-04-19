import requests
import random
import time

numeros = ['004', '008', '010', '012', '016', '020', '024', '028', '031', '032', '036', '040', '044', '048', '050', '051', '052', '056', '060', '064', '068', '070', '072', '074', '076', '084', '086', '090', '092', '096', '100', '104', '108', '112', '116', '120', '124', '132', '136', '140', '144', '148', '152', '156', '158', '162', '166', '170', '174', '175', '178', '180', '184', '188', '191', '192', '196', '203', '204', '208', '212', '214', '218', '222', '226', '231', '232', '233', '234', '238', '239', '242', '246', '248', '250', '254', '258', '260', '262', '266', '268', '270', '275', '276', '288', '292', '296', '300', '304', '308', '312', '316', '320', '324', '328', '332', '334', '336', '340', '344', '348', '352', '356', '360', '364', '368', '372', '376', '380', '384', '388', '392', '398', '400', '404', '408', '410', '414', '417', '418', '422', '426', '428', '430', '434', '438', '440', '442', '446', '450', '454', '458', '462', '466', '470', '474', '478', '480', '484', '492', '496', '498', '499', '500', '504', '508', '512', '516', '520', '524', '528', '531', '533', '534', '535', '540', '548', '554', '558', '562', '566', '570', '574', '578', '580', '581', '583', '584', '585', '586', '591', '598', '600', '604', '608', '612', '616', '620', '624', '626', '630', '634', '638', '642', '643', '646', '652', '654', '659', '660', '662', '663', '666', '670', '674', '678', '682', '686', '688', '690', '694', '702', '703', '704', '705', '706', '710', '716', '724', '728', '729', '732', '740', '744', '748', '752', '756', '760', '762', '764', '768', '772', '776', '780', '784', '788', '792', '795', '796', '798', '800', '804', '807', '818', '826', '831', '832', '833', '834', '840', '850', '854', '858', '860', '862', '876', '882', '887', '894']

# Tamaño máximo del cache
MAX_CACHE_SIZE = 600

# Diccionario para almacenar las respuestas de las solicitudes
cache = {}

# Lista para llevar un registro de los números aleatorios generados y su orden de uso
cache_order = []

def realizar_solicitud(numero_aleatorio):
    start_time = time.time() # Tiempo de inicio de la solicitud
    print("Número aleatorio:", numero_aleatorio)
    # Verificar si la respuesta está en el cache
    if numero_aleatorio in cache:
        response_text = cache[numero_aleatorio]
        # Mover el número aleatorio al final de la lista
        cache_order.remove(numero_aleatorio)
        cache_order.append(numero_aleatorio)
    else:
        print(f'Cache miss for {numero_aleatorio}')
        response = requests.get(f'https://restcountries.com/v3.1/alpha/{numero_aleatorio}')

        if response.status_code == 200:
            response_text = response.text
            # Agregar el número aleatorio y la respuesta al cache
            if len(cache) >= MAX_CACHE_SIZE:
                # Eliminar la entrada LRU del cache
                lru_num = cache_order.pop(0)
                del cache[lru_num]
            cache[numero_aleatorio] = response_text
            # Agregar el número aleatorio al final de la lista
            cache_order.append(numero_aleatorio)
        else:
            response_text = f'Error en la solicitud: {response.status_code}'

    print(response_text)
    end_time = time.time()  # Tiempo de finalización de la solicitud
    tiemporespuesta= start_time - end_time
    print(tiemporespuesta)

for _ in range(100):
    numero_aleatorio = random.choice(numeros)
    realizar_solicitud(numero_aleatorio)
    
