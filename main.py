import requests

url = 'https://midas.minsal.cl/farmacia_v2/WS/getLocalesTurnos.php'

respuesta = requests.get(url)
farmacias = respuesta.json()

for famarcia in farmacias:
    if famarcia["comuna_nombre"] == "INDEPENDENCIA":
        print(famarcia["local_nombre"],famarcia["local_direccion"],famarcia["comuna_nombre"])