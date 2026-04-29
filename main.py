import pandas as pd 

from utils.simulacionComercio import simulacion_datos_comercio

from notebook.limpiezaComercio import limpiar_comercio

datos=simulacion_datos_comercio(200)

simulaciones_ordenadas=pd.DataFrame(datos)

simulaciones_limpias=limpiar_comercio(simulaciones_ordenadas)

print(simulaciones_limpias)