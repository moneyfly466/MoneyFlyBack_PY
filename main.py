from utils.simulacionUsuarios import simulacion_datos_usuario
import pandas as pd

#imprimir datos sin pandas
#resultado = (simulacion_datos_usuario(500))
#print (resultado)

#imprimir datos con pandas
datos = (simulacion_datos_usuario(500))
tabla_ordenada = pd.DataFrame(datos)

print(tabla_ordenada)