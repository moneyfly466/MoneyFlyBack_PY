import os
import pandas as pd

RUTA_PUBLIC = os.environ.get(
    "RUTA_PUBLIC",
    os.path.join(os.path.dirname(__file__), "..", "..", "MoneyFlyFrontend", "public", "resultados")
)

def transformar_datos(dataframe_limpio):

    # ── Filtro 1: Usuarios mayores de 50 por género ──
    filtro1 = dataframe_limpio.query("edad > 50")
    agrupacion1 = filtro1.groupby("genero")["id"].count().reset_index(name="cuenta")

    # ── Filtro 2: Agrupar por tipo de documento ──
    agrupacion2 = dataframe_limpio.groupby("tipoDocumento")["id"].count().reset_index(name="cantidad")

    # ── Filtro 3: Ocupaciones con más de 20 usuarios ──
    agrupacion3 = (
        dataframe_limpio.groupby("ocupacion")["id"]
        .count()
        .reset_index(name="total")
        .query("total > 20")
    )

    # ── Filtro 4: Correos de dominio Gmail ──
    filtro4 = dataframe_limpio[dataframe_limpio["correo"].str.contains("gmail", case=False, na=False)]
    agrupacion4 = filtro4.groupby("ocupacion")["id"].count().reset_index(name="cuenta")

    # ── Filtro 5: Distribución de edades por grupos ──
    dataframe_limpio = dataframe_limpio.copy()
    dataframe_limpio["grupo_edad"] = pd.cut(
        dataframe_limpio["edad"],
        bins=[0, 12, 18, 30, 50, 70, 100],
        labels=["Niño", "Adolescente", "Joven", "Adulto", "Adulto mayor", "Senior"]
    )
    agrupacion5 = dataframe_limpio.groupby("grupo_edad")["id"].count().reset_index(name="usuarios")


    os.makedirs(RUTA_PUBLIC, exist_ok=True)

    agrupacion1.to_json(
        os.path.join(RUTA_PUBLIC, "mayores_50_por_genero.json"),
        orient="records", force_ascii=False
    )
    agrupacion2.to_json(
        os.path.join(RUTA_PUBLIC, "usuarios_por_tipo_doc.json"),
        orient="records", force_ascii=False
    )
    agrupacion3.to_json(
        os.path.join(RUTA_PUBLIC, "ocupaciones_mas_20.json"),
        orient="records", force_ascii=False
    )
    agrupacion4.to_json(
        os.path.join(RUTA_PUBLIC, "gmail_por_ocupacion.json"),
        orient="records", force_ascii=False
    )
    agrupacion5.to_json(
        os.path.join(RUTA_PUBLIC, "usuarios_por_grupo_edad.json"),
        orient="records", force_ascii=False
    )

    print(">>> JSON de usuarios exportados correctamente en public/resultados/")

    return {
        "mayores_50_por_genero": agrupacion1,
        "usuarios_por_tipo_doc": agrupacion2,
        "ocupaciones_mas_20":    agrupacion3,
        "gmail_por_ocupacion":   agrupacion4,
        "usuarios_por_grupo_edad": agrupacion5
    }