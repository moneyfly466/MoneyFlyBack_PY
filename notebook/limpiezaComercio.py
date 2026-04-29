import pandas as pd

def limpiar_comercio(dato_sucio):
    dato_limpio=dato_sucio.copy()

    #Para limpiar texto y espacios en blanco y colocar todo en minusculas
    columnas_textos=["actividad", "sectorComercial", "ubicacion"]
    for  columna in columnas_textos:
        dato_limpio[columna]=dato_limpio[columna].astype("string").str.strip().str.lower()


    #limpiar los textos  solamente esperados
    actividades_esperadas=["venta", "servicios", "tecnologia", "salud", "retail"]
    dato_limpio["actividad"]=dato_limpio["actividad"].where(
        dato_limpio["actividad"].isin(actividades_esperadas),
        pd.NA
    )

    #Evaluar que las columnas si sean numericas
    dato_limpio["id"]=pd.to_numeric(dato_limpio["id"])
    dato_limpio["costo"]=pd.to_numeric(dato_limpio["totalGastado"])
    dato_limpio["costo"]=pd.to_numeric(dato_limpio["gastoPromedio"])


    #evaluar solo valores numericos permitidos
    dato_limpio=dato_limpio[dato_limpio["id"]>0]
    dato_limpio=dato_limpio[dato_limpio["totalGastado"]>0]
    dato_limpio=dato_limpio[dato_limpio["gastoPromedio"]>0]

    #que la fecha si sea una fecha
    dato_limpio["fechaGasto"]=pd.to_datetime(dato_limpio["fechaGasto"])


    #reemplazar una fecha por defecto si el campo llego vacio
    fecha_default = pd.to_datetime("2026-01-01")
    dato_limpio["fechaGasto"] = dato_limpio["fechaGasto"].fillna(fecha_default)

    #rutina para evaluar campos obligatorios
    columnas_obligatorias = ["id", "nombre", "actividad", "ubicacion", "sectorComercial"]
    dato_limpio = dato_limpio.dropna(subset=columnas_obligatorias)


    return dato_limpio

