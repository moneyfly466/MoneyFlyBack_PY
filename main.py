import pandas as pd

from notebook.consumoUsuario import consumir_api_usuario
from notebook.limpiezaUsuario import limpiar_usuarios
from notebook.transformacionUsuario import transformar_datos
from notebook.graficacionUsuario import graficar_lineas, graficar_barras, graficar_torta, graficar_mapa_calor

datos_tablas_usuario=consumir_api_usuario()
data_frame_usuario=pd.DataFrame(datos_tablas_usuario)
data_frame_limpio_usuario=limpiar_usuarios(data_frame_usuario)
agrupaciones=transformar_datos(data_frame_limpio_usuario)

# 1. Gráfico de líneas: usuarios mayores de 50 (Columna de valor: "cuenta")
graficar_lineas(
    agrupaciones["mayores_50_por_genero"],
    columna_eje_x="genero",
    columna_eje_y="cuenta",  # Cambiado de "id" a "cuenta"
    titulo="usuarios mayores de 50",
    color_linea="#2196F3",
    nombre_archivo="lineas_mayores_50.png"
)

# 2. Gráfico de barras: agrupar por tipo de documento (Columna de valor: "cantidad")
graficar_barras(
    agrupaciones["usuarios_por_tipo_doc"], # Cambiado el nombre de la llave para coincidir con transformar_datos
    columna_categorias="tipoDocumento",
    columna_valores="cantidad",  # Cambiado de "id" a "cantidad"
    titulo="agrupar por tipo de documento",
    color_barras="#4CAF50",
    nombre_archivo="barras_tipoDocumento.png"
)

# 3. Gráfico de torta: proporción de tipo de documento más usado (Columna de valor: "cantidad")
graficar_torta(
    agrupaciones["usuarios_por_tipo_doc"], # Cambiado el nombre de la llave para coincidir con transformar_datos
    columna_etiquetas="tipoDocumento",
    columna_valores="cantidad",  # Cambiado de "id" a "cantidad"
    titulo="tipo de documento mas usadado",
    nombre_archivo="torta_servicios.png"
)


