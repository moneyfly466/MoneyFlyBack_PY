import pandas as pd

def limpiar_usuarios(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy()

    # 1. Eliminar espacios y pasar todo a minúsculas (Mantiene tu lógica original)
    data_frame_limpio["nombres"] = data_frame_limpio["nombres"].astype("string").str.strip().str.lower()
    data_frame_limpio["tipoDocumento"] = data_frame_limpio["tipoDocumento"].astype("string").str.strip().str.lower()
    data_frame_limpio["correo"] = data_frame_limpio["correo"].astype("string").str.strip().str.lower()
    data_frame_limpio["contraseña"] = data_frame_limpio["contraseña"].astype("string").str.strip().str.lower()
    data_frame_limpio["genero"] = data_frame_limpio["genero"].astype("string").str.strip().str.lower()
    data_frame_limpio["ocupacion"] = data_frame_limpio["ocupacion"].astype("string").str.strip().str.lower()
    data_frame_limpio["documento"] = data_frame_limpio["documento"].astype("string").str.strip().str.lower()
    data_frame_limpio["telefono"] = data_frame_limpio["telefono"].astype("string").str.strip().str.lower()

    # 2. Limpiar los datos para controlar valores esperados
    # ADAPTACIÓN: Valores pasados a minúsculas para que no se borren tras el .str.lower()
    valores_esperados_nombres = ["juan perez", "maria gomez", "carlos ramirez", "ana torres", "luis martinez", "sofia herrera", "pedro castillo", "valentina diaz", "jorge suarez", "laura beltran"]
    data_frame_limpio["nombres"] = data_frame_limpio["nombres"].where( 
        data_frame_limpio["nombres"].isin(valores_esperados_nombres), pd.NA
    )

    # ADAPTACIÓN: Corregido "tarjeta de identidad" que tenía un error de tipeo previo
    valores_esperados_tipoDocumento = ["cedula", "tarjeta de identidad", "pasaporte"]
    data_frame_limpio["tipoDocumento"] = data_frame_limpio["tipoDocumento"].where(
        data_frame_limpio["tipoDocumento"].isin(valores_esperados_tipoDocumento), pd.NA
    )

    # ADAPTACIÓN: Como tu precarga en Java genera correos automáticos dinámicos (usuario0@correo.com, usuario1@correo.com...), 
    # si dejas una lista fija te borrará todos los usuarios. Cambiamos a validar el patrón que tú mismo definiste en Java:
    data_frame_limpio["correo"] = data_frame_limpio["correo"].where(
        data_frame_limpio["correo"].str.contains("@correo.com", na=False), pd.NA
    )

    # ADAPTACIÓN: Igual que el correo, tus contraseñas de Java son dinámicas ("pass0", "pass1"...). 
    # Validamos que sigan el patrón lógico que creaste en tu inicializador de Spring Boot:
    data_frame_limpio["contraseña"] = data_frame_limpio["contraseña"].where(
        data_frame_limpio["contraseña"].str.startswith("pass", na=False), pd.NA
    )

    # ADAPTACIÓN: Al usar Enums en Java (.values()), Spring Boot devuelve los nombres del Enum.
    # Agregamos los formatos estándar de enums en minúsculas para asegurar coincidencia
    valores_esperados_generos = ["hombre", "mujer", "masculino", "femenino", "otro", "prefiero no decirlo"]
    data_frame_limpio["genero"] = data_frame_limpio["genero"].where(
        data_frame_limpio["genero"].isin(valores_esperados_generos), pd.NA
    )

    # ADAPTACIÓN: Valores pasados a minúsculas para emparejar con el .str.lower()
    valores_esperados_ocupaciones = ["ingeniero", "profesor", "estudiante", "medico", "abogado", "comerciante", "administrador", "diseñador", "programador", "contador"]
    data_frame_limpio["ocupacion"] = data_frame_limpio["ocupacion"].where(
        data_frame_limpio["ocupacion"].isin(valores_esperados_ocupaciones), pd.NA
    )

    # ADAPTACIÓN: En Java generas documentos aleatorios de 8 dígitos entre 10000000 y 99999999.
    # Si dejas la lista fija ["11111"...], se borrarían todos. Validamos que sean puramente números:
    data_frame_limpio["documento"] = data_frame_limpio["documento"].where(
        data_frame_limpio["documento"].str.isnumeric(), pd.NA
    )

    # ADAPTACIÓN: En Java generas teléfonos que empiezan con "300". Validamos que cumplan con esa regla
    # para que tu lista vacía original no destruya todos los registros telefónicos analizados:
    data_frame_limpio["telefono"] = data_frame_limpio["telefono"].where(
        data_frame_limpio["telefono"].str.startswith("300", na=False), pd.NA
    )

    # 3. Verificar que los números sí sean números
    data_frame_limpio["id"] = pd.to_numeric(data_frame_limpio["id"], errors='coerce')
    data_frame_limpio["edad"] = pd.to_numeric(data_frame_limpio["edad"], errors='coerce')

    # 4. Verificar los valores numéricos esperados
    data_frame_limpio = data_frame_limpio[data_frame_limpio["id"] > 0]
    data_frame_limpio = data_frame_limpio[data_frame_limpio["edad"] >= 10] 

    return data_frame_limpio