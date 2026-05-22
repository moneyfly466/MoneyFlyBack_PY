import pandas as pd

def transformar_datos(data_frame_limpio):

    # ─────────────────────────────────────────────
    # Transformación 6:
    # Gastos del sector tecnológico por fecha
    # Ideal para gráfica de líneas o barras
    # ─────────────────────────────────────────────
    
    filtro6 = data_frame_limpio.query(
        "sectorComercial == 'tecnologico'"
    )

    agrupacion6 = (
        filtro6
        .groupby("fechaGasto")["id"]
        .count()
        .reset_index(name="conteo")
    )

    # ─────────────────────────────────────────────
    # Transformación 7:
    # Comercios con alto gasto
    # Ideal para gráfica de barras
    # ─────────────────────────────────────────────
    
    filtro7 = data_frame_limpio.query(
        "totalGastado >= 25000"
    )

    agrupacion7 = (
        filtro7
        .groupby("ubicacion")["id"]
        .count()
        .reset_index(name="conteo")
    )

    # ─────────────────────────────────────────────
    # Transformación 8:
    # Sector comercial vs ubicación
    # Ideal para mapa de calor
    # ─────────────────────────────────────────────
    
    filtro8 = data_frame_limpio.query(
        "gastoPromedio >= 5000"
    )

    agrupacion8 = (
        filtro8
        .groupby(["sectorComercial", "ubicacion"])["id"]
        .count()
        .reset_index(name="conteo")
    )

    # resumen de agrupaciones
    agrupacion_resumen = {
        "agrupacion6": agrupacion6,
        "agrupacion7": agrupacion7,
        "agrupacion8": agrupacion8
    }

    return agrupacion_resumen