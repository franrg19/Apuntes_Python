#CREAME UN DICCIONARIO
persona={
    "nombre": "Fran",
    "edad": 33,
    "registrado": True,
}
print(persona)
#ACCEDEME A UN VALOR POR SU CLAVE
print(persona["edad"])

#AÑADIR UNA NUEVA CLAVE VALOR

persona["ciudad"] = "Málaga"
persona["numero de hijos"] = "0"

print(persona)

#CAMBIAR EL VALOR DE UNA CLAVE

persona["ciudad"] = "cadiz"
persona["numero de hijos"] = 1

print (persona)


#ELIMINAR UNA CLAVE

del persona ["ciudad"]
print(persona)

#COMPROBAR SI UNA CLAVE YA EXISTE
existe_name = "nombre" in persona
print(existe_name)

existe_edad = "edad" in persona
print(existe_edad)

existe_fran = "fran" in persona ["nombre" ]

#COMPARAR DOS VALORES BOOLEANOS
es_menor_y_registrado = persona["edad"] <18 and persona ["registrado"] == True
print(es_menor_y_registrado)

#USAR NOT CON UN BOOLEANO
no_veo_registro = not persona["registrado"]
print(no_veo_registro)

#CREAME UN CONJUNTO A PARTIR DE UNA LISTA DE DUPLICADOS
numeritos=[1,2,3,4,5,6,7,2,6,8,1,3,5]

#convierto a conjunto. Asi elimino duplicados
conjuntito= set(numeritos)
print(conjuntito)

#COMPARAR SI DOS COLECCIONES TIENEN LOS MISMOS ELEMENTOS UNICOS
coleccion_a = set([1,2,3,4])
coleccion_b=set([3,2,1])

mismos_elementitos = coleccion_a == coleccion_b
print(mismos_elementitos)