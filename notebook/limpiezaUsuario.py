import pandas as pd

def limpiar_usuarios(data_frame_sucio):
    data_frame_limpio=data_frame_sucio.copy()

    #eliminar espacios y todo en mayusculas
    data_frame_limpio["nombre"]=data_frame_limpio["nombre"].astype("string").str.strip().str.lower()
    data_frame_limpio["tipoDocumento"]=data_frame_limpio["tipoDocumento"].astype("string").str.strip().str.lower()
    data_frame_limpio["correo"]=data_frame_limpio["correo"].astype("string").str.strip().str.lower()
    data_frame_limpio["contraseña"]=data_frame_limpio["contraseña"].astype("string").str.strip().str.lower()
    data_frame_limpio["genero"]=data_frame_limpio["genero"].astype("string").str.strip().str.lower()
    data_frame_limpio["ocupacion"]=data_frame_limpio["ocupacion"].astype("string").str.strip().str.lower()
    data_frame_limpio["documento"]=data_frame_limpio["documento"].astype("string").str.strip().str.lower()
    data_frame_limpio["telefono"]=data_frame_limpio["telefono"].astype("string").str.strip().str.lower()

    #limpiar los datos para controlar valores eperados
    valores_esperados_nombres=["juan","maria","andres","santiago","daniel","isabel","clara"]
    data_frame_limpio["nombre"]=data_frame_limpio["nombre"].where( 
        data_frame_limpio["nombre"].isin(valores_esperados_nombres),pd.NA
    )

    valores_esperados_tipoDocumento=["cedula","targenta de identidad","pasaporte"]
    data_frame_limpio["tipoDocumnto"]=data_frame_limpio["tipoDocumento"].where(
        data_frame_limpio["tipoDocumento"].isin(valores_esperados_tipoDocumento),pd.NA
    )

    valores_esperados_correos=["juan@gmail.com","maria@gmail.com","andres@gmail.com","santiago@gmail.com","daniel@gmail.com","isabel@gmail.com","clara@gmail.com"]
    data_frame_limpio["correo"]=data_frame_limpio["correo"].where(
        data_frame_limpio["correo"].isin(valores_esperados_correos),pd.NA
    )

    valores_esperados_contraseñas=["hola123","chao123","once:once","sapo123","perro123"]
    data_frame_limpio["contraseña"]=data_frame_limpio["contraseña"].where(
        data_frame_limpio["contraseña"].isin(valores_esperados_contraseñas),pd.NA
    )

    valores_esperados_generos=["hombre","mujer","prefiero no decirlo"]
    data_frame_limpio["genero"]=data_frame_limpio["genero"].where(
        data_frame_limpio["genero"].isin(valores_esperados_generos),pd.NA
    )

    valores_esperados_ocupaciones=["vendedor","programador","facturador","estudiante","medico"]
    data_frame_limpio["ocupacion"]=data_frame_limpio["ocupacion"].where(
        data_frame_limpio["ocupacion"].isin(valores_esperados_ocupaciones),pd.NA
    )

    valores_esperados_documentos=["11111","22222","33333","44444","5555"]
    data_frame_limpio["documento"]=data_frame_limpio["documento"].where(
        data_frame_limpio["documento"].isin(valores_esperados_documentos),pd.NA
    )

    valores_esperados_telefonos=[]
    data_frame_limpio["telefono"]=data_frame_limpio["telefono"].where(
        data_frame_limpio["telefono"].isin(valores_esperados_telefonos),pd.NA
    )

    #verificar que los numeros si sean numeros
    data_frame_limpio["id"]=pd.to_numeric(data_frame_limpio["id"])
    data_frame_limpio["edad"]=pd.to_numeric(data_frame_limpio["edad"])

    #vefificar los valores numericos esperados
    data_frame_limpio=data_frame_limpio[data_frame_limpio["id"]>0]
    data_frame_limpio=data_frame_limpio[data_frame_limpio["edad"]>=10]