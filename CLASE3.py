#1 LONGITUD DE UNA CADENA
import random

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

#4.REMPLAZAR PALABRAS EN UNA CADENA
frase="me gusta java yuju"
print("cambio la palabra: ",frase.replace("java","python"))

#5.VERIFICAR SI UNA CADENA EXISTE
print("python" in frase)
nueva_frase="Python"
print("esto es: ", nueva_frase)

#6.UNIR VARIAS PALABRAS EN UNA CADENA
palabras =["hola","mundo","en","Python"]
print("frase completa con join; "," ".join(palabras) )

#7.SPLIT
oracion="Python es divertido"
palabritas = oracion.split() # ["Python","es","divertido"]
print("lista de palabras  ", palabritas)

#8.REDONDEAR UN NUMERO DECIMAL
numero = 3.1416
print("Mi numero redeondeado es: " , round(numero,1))

#9.FORMATEO DE NUMEROS DECIMALES
precio = 19.99
print("el precio con dos decimales: {:.2f}".format(precio))

#10.OBTENER EL VALOS ASCII DE UN CARACTER
print("esto es el codigo ASCII de 'A': ",ord('A'))

#11.ELEVAR AL CUADRADO
numero_al_cuadrado = 5
print("5 al cuadrado es: ", numero_al_cuadrado ** 3)

#12.RAIZ CUADRADA
print("La raiz cuadrada de 25 es: ", 16 ** 0.5)
import math
numerito = 100
raiz= math.sqrt(numerito)
print("La raiz de 100 es: ", raiz)

#13. DIVISIONES
print("division normal: ", 10/3)
print("division entera: ", 10//3)
print("Resto: ", 10%3)

#14 GENERAR UN NUMERO ALEATORIO
print("numero aleatorio entre 1 y 10: ",random.randint(1,10) )

#15.CONVERTIR NUMEROS A CADENAS Y VICEVERSA
numerajo = 300
texto= str(numerajo)
print("convertir a texto, soy: ",texto)
cadena=200
numerajo= int(cadena)
print("convertido a numero soy: ", numerajo)

#16.REDONDEAR HACIA ARRIBA
print("redondeo hacia arruba del 3.6: ",math.ceil(3.6))
print("redondeo hacia abajo del 3.2: ",math.floor(3.2))

#17 CONVERTIR UNA LISTA EN UN CONJUNTO, ES DECIR ELIMINAR DUPLICADOS
numeroides = [1,2,3,3,4,5,5]
sin_duplicados = set(numeroides)
print("La lista sin duplicados es:", sin_duplicados)

#18.REPETIR UNA CADENA
print("python !" *3 )

#19.TIPO DE DATO
dato = 3.14
print("El tipo de variable de dato es: ", type(dato))

#20. COMBINAR CADENAS Y VARIABLES EN UN PRINT
name = "Fran"
edad = "33"
print(f"Hola, soy {name} y tengo {edad} años")
