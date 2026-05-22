import pandas as pd

def transformar_datos(dataframe_limpio):
    
    # ----------------------
    # Filtro 1: Usuarios mayores de 50 años
    # ----------------------
    filtro1 = dataframe_limpio.query("edad > 50")
    agrupacion1 = filtro1.groupby("genero")["id"].count().reset_index(name="cuenta")
    
    # ----------------------
    # Filtro 2: Agrupar por tipo de documento
    # ----------------------
    filtro2 = dataframe_limpio.copy()
    agrupacion2 = filtro2.groupby("tipoDocumento")["id"].count().reset_index(name="cantidad")

    # ----------------------
    # Filtro 3: Ocupaciones con más de 20 usuarios
    # ----------------------
    filtro3 = dataframe_limpio.copy()
    agrupacion3 = (
        filtro3.groupby("ocupacion")["id"]
        .count()
        .reset_index(name="total")
        .query("total > 20")
    )

    # ----------------------
    # Filtro 4: Correos de dominio Gmail
    # ----------------------
    filtro4 = dataframe_limpio[dataframe_limpio["correo"].str.contains("gmail", case=False)]
    agrupacion4 = filtro4.groupby("ocupacion")["id"].count().reset_index(name="cuenta")

    # ----------------------
    # Filtro 5: Distribución de edades por grupos
    # ----------------------
    dataframe_limpio["grupo_edad"] = pd.cut(
        dataframe_limpio["edad"],
        bins=[0, 12, 18, 30, 50, 70, 100],
        labels=["Niño", "Adolescente", "Joven", "Adulto", "Adulto mayor", "Senior"]
    )
    filtro5 = dataframe_limpio
    agrupacion5 = filtro5.groupby("grupo_edad")["id"].count().reset_index(name="usuarios")

    # ----------------------
    # Resultado final
    # ----------------------
    resultado = {
        "mayores_50_por_genero": agrupacion1,
        "usuarios_por_tipo_doc": agrupacion2,
        "ocupaciones_mas_20": agrupacion3,
        "gmail_por_ocupacion": agrupacion4,
        "usuarios_por_grupo_edad": agrupacion5
    }

    return resultado