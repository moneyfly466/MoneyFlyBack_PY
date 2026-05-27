import os
import pandas as pd

from notebook.consumoUsuario   import consumir_api_usuario
from notebook.consumoComercio  import consumir_api_comercio
from notebook.limpiezaUsuario  import limpiar_usuarios
from notebook.limpiezaComercio import limpiar_comercio
from notebook.transformacionUsuario import transformar_datos as transformar_usuarios
from notebook.transformacionComercio import transformar_datos as transformar_comercio
from notebook.graficacionUsuario import graficar_lineas, graficar_barras, graficar_torta
from notebook.graficacionComercio import (
    graficar_lineas  as graficar_lineas_comercio,
    graficar_barras  as graficar_barras_comercio,
    graficar_mapa_calor
)

# ── USUARIOS ──────────────────────────────────────────────────────
print("Consumiendo API de usuarios...")
datos_usuario    = consumir_api_usuario()
df_usuario       = pd.DataFrame(datos_usuario)
df_limpio_usuario = limpiar_usuarios(df_usuario)
agrupaciones_usuario = transformar_usuarios(df_limpio_usuario)

# ── COMERCIO ──────────────────────────────────────────────────────
print("Consumiendo API de comercio...")
datos_comercio    = consumir_api_comercio()
df_comercio       = pd.DataFrame(datos_comercio)
df_limpio_comercio = limpiar_comercio(df_comercio)
agrupaciones_comercio = transformar_comercio(df_limpio_comercio)

# ── GRÁFICAS USUARIOS ─────────────────────────────────────────────

# 1. Líneas: usuarios mayores de 50 por género
graficar_lineas(
    agrupaciones_usuario["mayores_50_por_genero"],
    columna_eje_x="genero",
    columna_eje_y="cuenta",
    titulo="Usuarios mayores de 50 por género",
    color_linea="#2196F3",
    nombre_archivo="lineas_mayores_50.png"
)

# 2. Barras: usuarios por tipo de documento
graficar_barras(
    agrupaciones_usuario["usuarios_por_tipo_doc"],
    columna_categorias="tipoDocumento",
    columna_valores="cantidad",
    titulo="Usuarios por tipo de documento",
    color_barras="#4CAF50",
    nombre_archivo="barras_tipoDocumento.png"
)

# 3. Torta: proporción de tipo de documento
graficar_torta(
    agrupaciones_usuario["usuarios_por_tipo_doc"],
    columna_etiquetas="tipoDocumento",
    columna_valores="cantidad",
    titulo="Proporción de tipo de documento",
    nombre_archivo="torta_tipoDocumento.png"
)

# ── GRÁFICAS COMERCIO ─────────────────────────────────────────────

# 4. Líneas: comercios del sector tecnológico por fecha
graficar_lineas_comercio(
    agrupaciones_comercio["agrupacion6"],
    columna_eje_x="fechaGasto",
    columna_eje_y="conteo",
    titulo="Comercios tecnológicos por fecha",
    color_linea="#FF9800",
    nombre_archivo="lineas_comercio_tecnologico.png"
)

# 5. Barras: comercios con alto gasto por ubicación
graficar_barras_comercio(
    agrupaciones_comercio["agrupacion7"],
    columna_categorias="ubicacion",
    columna_valores="conteo",
    titulo="Comercios con alto gasto por ubicación",
    color_barras="#E91E63",
    nombre_archivo="barras_comercio_ubicacion.png"
)

# 

print("¡Proceso completado!")