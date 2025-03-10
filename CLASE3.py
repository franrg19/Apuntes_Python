#1 LONGITUD DE UNA CADENA

nombre ="Fran Rebollo"
print("Longitud del nombre: ", len(nombre) )

#2. CONVERTIR TEXTO A MAYUSCULAS Y MINUSCULAS
#UPPER
print("Esto soy yo en mayusculas ", nombre.upper())
#LOWER
print("Esto soy yo en minusculas ", nombre.lower())

#3.SLICE
print("primeros 3 caracteres: ", nombre[:3])
print("ultimos 4 caracteres: ", nombre[-4:])

#REMPLAZAR PALABRAS EN UNA CADENA
frase="me gusta java yuju"
print("cambio la palabra: ",frase.replace("java","python"))

#VERIFICAR SI UNA CADENA EXISTE
print("python" in frase)
nueva_frase="Python"
print("esto es: ", nueva_frase)
