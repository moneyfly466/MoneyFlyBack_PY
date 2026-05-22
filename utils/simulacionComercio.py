# id (integer)
# nit (string)
# nombre (string)
# actividad (string)
# contacto (string)
# totalGastado (float)
# ubicacion (string)
# gastoPromedio (float)
# sectorComercial (string)
# fechaGasto (localdate → string formato YYYY-MM-DD)

import random
from datetime import datetime, timedelta

def simulacion_datos_comercio(numeroDatos):

    # atributos basea
    nits        = ["900123456", "901234567", "902345678", "903456789", "904567890"]
    nombres     = ["Tienda ABC", "Supermercado XYZ", "Tech Store", "Farmacia Vida", "Ropa Express"]
    actividades = ["venta", "servicios", "tecnologia", "salud", "retail"]
    contactos   = ["contacto@abc.com", "info@xyz.com", "ventas@tech.com", "salud@vida.com", "express@ropa.com"]
    ubicaciones = ["Bogotá", "Medellín", "Cali", "Barranquilla", "Cartagena"]
    sectores    = ["comercial", "industrial", "tecnologico", "salud", "retail"]
    fechaGasto = datetime(2026,1,1)

    # valores inválidos para errores controlados
    actividades_invalidas  = ["curso de cocina", "clase de yoga"]
    contactos_invalidos    = ["noesuncorreo", "@@mal.com"]
    ubicaciones_invalidas  = ["Narnia", "Ciudad Gótica"]

    datos = []

    for _ in range(numeroDatos):
        total_gastado  = round(random.uniform(1000, 50000), 2)
        gasto_promedio = round(total_gastado / random.randint(1, 10), 2)

   

        dato = {
            "id":              random.randint(1, 500),
            "nit":             random.choice(nits),
            "nombre":          random.choice(nombres),
            "actividad":       random.choice(actividades),
            "contacto":        random.choice(contactos),
            "totalGastado":    total_gastado,
            "ubicacion":       random.choice(ubicaciones),
            "gastoPromedio":   gasto_promedio,
            "sectorComercial": random.choice(sectores),
            "fechaGasto":      fechaGasto+timedelta(days=random.randint(0,60))
        }

        # ─── Inyección de errores controlados ───────────────────────────
        probabilidadError = random.random()

        if probabilidadError < 0.10:                                  
            dato["id"] = None

        elif probabilidadError < 0.20:                               
            dato["nit"] = " " + dato["nit"].upper()

        elif probabilidadError < 0.35:                                 
            dato["actividad"] = random.choice(actividades_invalidas)

        elif probabilidadError < 0.45:                                 
            dato["contacto"] = random.choice(contactos_invalidos)

        elif probabilidadError < 0.55:                                 
            dato["totalGastado"] = random.choice([0, -5000, None])

        elif probabilidadError < 0.65:                                 
            dato["ubicacion"] = random.choice(ubicaciones_invalidas)

        elif probabilidadError < 0.75:                                 
            dato["gastoPromedio"] = random.choice([0, -1000, None])

        elif probabilidadError < 0.85:                                
            dato["sectorComercial"] = None

        elif probabilidadError < 0.95:                               
            dato["fechaGasto"] = None

      
        datos.append(dato)

    return datos