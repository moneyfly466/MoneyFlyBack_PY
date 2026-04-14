#id (integer)
#nit (string)
#nombre (string)
#actividad (string)
#contacto (string)
#totalGastado (integer)
#ubicacion (string)
#gastoPromedio (integer)
#sectorComercial (string)
#fechaGasto (localdate)


import random
from datetime import datetime, timedelta

def simulacion_datos_comercio(numeroDatos):

    # atributos base
    nits = ["900123456", "901234567", "902345678", "903456789"]
    nombres = ["Tienda ABC", "Supermercado XYZ", "Tech Store", "Farmacia Vida", "Ropa Express"]
    actividades = ["venta", "servicios", "tecnologia", "salud", "retail"]
    contactos = ["contacto@abc.com", "info@xyz.com", "ventas@tech.com", "salud@vida.com"]
    ubicaciones = ["Bogotá", "Medellín", "Cali", "Barranquilla"]
    sectores = ["comercial", "industrial", "tecnologico", "salud"]

    datos = []

    for _ in range(numeroDatos):
        total_gastado = round(random.uniform(1000, 50000), 2)
        gasto_promedio = round(total_gastado / random.randint(1, 10), 2)

        # generar fecha aleatoria
        fecha_base = datetime.now()
        fecha_aleatoria = fecha_base - timedelta(days=random.randint(0, 365))

        dato = {
            "id": random.randint(1, 500),
            "nit": random.choice(nits),
            "nombre": random.choice(nombres),
            "actividad": random.choice(actividades),
            "contacto": random.choice(contactos),
            "totalGastado": total_gastado,
            "ubicacion": random.choice(ubicaciones),
            "gastoPromedio": gasto_promedio,
            "sectorComercial": random.choice(sectores),
            "fechaGasto": fecha_aleatoria.strftime("%Y-%m-%d")
        }

        datos.append(dato)

    return datos