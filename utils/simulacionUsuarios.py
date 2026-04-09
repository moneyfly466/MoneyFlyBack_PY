#id (integer)
#nombres (string) 
#tipo documento (string)
#documento (string) 
#edad (integer) 
#correo (string)
#telefono (string) 
#contraseña (string)
#genero (string)
#ocupacion (string)

import random 

def simulacion_datos_usuario(numeroDatos):

    #se definen los atributos bases

    nombres=["juan","maria","andres","santiago","daniel","isabel","clara"]
    tipoDocumentos=["cedula","targenta de identidad","pasaporte"]
    documentos=["11111","22222","33333","44444","5555"]
    correos=["juan@gmail.com","maria@gmail.com","andres@gmail.com","santiago@gmail.com","daniel@gmail.com","isabel@gmail.com","clara@gmail.com"]
    telefonos=["1234567890","0987654321","1123456789","122345678","334567890"]
    contraseñas=["hola123","chao123","once:once","sapo123","perro123"]
    generos=["hombre","mujer","prefiero no decirlo"]
    ocupaciones=["vendedor","programador","facturador","estudiante","medico"]

    datos=[]
    for _ in range (numeroDatos):
        dato={
            "id":random.randint(1,500),
            "nombre":random.choice(nombres),
            "tipoDocumento":random.choice(tipoDocumentos),
            "documento":random.choice(documentos),
            "edad":random.randint(0,100),
            "correo":random.choice(correos),
            "telefono":random.choice(telefonos),
            "contraseña":random.choice(contraseñas),
            "genero":random.choice(generos),
            "ocupacion":random.choice(ocupaciones)
        }
        datos.append(dato)
    return datos