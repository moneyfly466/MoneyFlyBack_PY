import requests

def consumir_api_comercio():
    url = "http://localhost:8080/apimoneyfly/v1/comercio"
    respuesta = requests.get(url)
    respuesta.raise_for_status()
    datos = respuesta.json()
    return datos