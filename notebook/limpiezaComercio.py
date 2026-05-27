import pandas as pd

def limpiar_comercio(dato_sucio):
    dato_limpio = dato_sucio.copy()

    # Limpiar texto: espacios en blanco y minúsculas
    columnas_textos = ["actividad", "sectorComercial", "ubicacion"]
    for columna in columnas_textos:
        dato_limpio[columna] = dato_limpio[columna].astype("string").str.strip().str.lower()

    # Filtrar solo actividades válidas
    actividades_esperadas = ["venta", "servicios", "tecnologia", "salud", "retail"]
    dato_limpio["actividad"] = dato_limpio["actividad"].where(
        dato_limpio["actividad"].isin(actividades_esperadas),
        pd.NA
    )

    # Evaluar que las columnas numéricas sí sean numéricas
    dato_limpio["id"] = pd.to_numeric(dato_limpio["id"], errors="coerce")

    # ✅ CORRECCIÓN: antes se sobreescribía "costo" dos veces con columnas distintas.
    # Ahora cada columna numérica se convierte de forma independiente y con su nombre correcto.
    dato_limpio["totalGastado"]  = pd.to_numeric(dato_limpio["totalGastado"],  errors="coerce")
    dato_limpio["gastoPromedio"] = pd.to_numeric(dato_limpio["gastoPromedio"], errors="coerce")

    # Filtrar solo valores numéricos permitidos (positivos)
    dato_limpio = dato_limpio[dato_limpio["id"]           > 0]
    dato_limpio = dato_limpio[dato_limpio["totalGastado"] > 0]
    dato_limpio = dato_limpio[dato_limpio["gastoPromedio"] > 0]

    # Convertir fechaGasto a tipo fecha
    dato_limpio["fechaGasto"] = pd.to_datetime(dato_limpio["fechaGasto"], errors="coerce")

    # Reemplazar fechas nulas por fecha por defecto
    fecha_default = pd.to_datetime("2026-01-01")
    dato_limpio["fechaGasto"] = dato_limpio["fechaGasto"].fillna(fecha_default)

    # Eliminar filas con campos obligatorios nulos
    columnas_obligatorias = ["id", "nombre", "actividad", "ubicacion", "sectorComercial"]
    dato_limpio = dato_limpio.dropna(subset=columnas_obligatorias)

    return dato_limpio