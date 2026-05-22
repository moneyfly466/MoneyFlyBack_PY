import requests

def consumir_api_usuario():
  url="http://localhost:8080/apimoneyfly/v1/usuarios"
  respuesta=requests.get(url)
  respuesta.raise_for_status()
  datos=respuesta.json()
  return datos
