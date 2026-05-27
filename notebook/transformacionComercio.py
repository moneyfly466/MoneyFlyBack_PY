import os
import pandas as pd


RUTA_PUBLIC = os.environ.get(
    "RUTA_PUBLIC",
    os.path.join(os.path.dirname(__file__), "..", "..", "MoneyFlyFrontend", "public", "resultados")
)

def transformar_datos(data_frame_limpio):

    # ─────────────────────────────────────────────
    # Transformación 6: Comercios tecnológicos por fecha
    # ─────────────────────────────────────────────
    filtro6 = data_frame_limpio.query("sectorComercial == 'tecnologico'")

    agrupacion6 = (
        filtro6
        .groupby("fechaGasto")["id"]
        .count()
        .reset_index(name="conteo")
    )
    # Convertir fechas a string para que sean serializables en JSON
    agrupacion6["fechaGasto"] = agrupacion6["fechaGasto"].astype(str)

    # ─────────────────────────────────────────────
    # Transformación 7: Comercios con alto gasto por ubicación
    # ─────────────────────────────────────────────
    filtro7 = data_frame_limpio.query("totalGastado >= 25000")

    agrupacion7 = (
        filtro7
        .groupby("ubicacion")["id"]
        .count()
        .reset_index(name="conteo")
    )

    # ─────────────────────────────────────────────
    # Transformación 8: Sector comercial vs ubicación
    # ─────────────────────────────────────────────
    filtro8 = data_frame_limpio.query("gastoPromedio >= 5000")

    agrupacion8 = (
        filtro8
        .groupby(["sectorComercial", "ubicacion"])["id"]
        .count()
        .reset_index(name="conteo")
    )

    os.makedirs(RUTA_PUBLIC, exist_ok=True)

    agrupacion6.to_json(
        os.path.join(RUTA_PUBLIC, "comercio_tecnologico_por_fecha.json"),
        orient="records", force_ascii=False
    )
    agrupacion7.to_json(
        os.path.join(RUTA_PUBLIC, "comercios_alto_gasto.json"),
        orient="records", force_ascii=False
    )
    agrupacion8.to_json(
        os.path.join(RUTA_PUBLIC, "sector_vs_ubicacion.json"),
        orient="records", force_ascii=False
    )

    print(">>> JSON de comercios exportados correctamente en public/resultados/")

    return {
        "agrupacion6": agrupacion6,
        "agrupacion7": agrupacion7,
        "agrupacion8": agrupacion8
    }