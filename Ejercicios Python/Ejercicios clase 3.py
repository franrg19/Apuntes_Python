import random
import math
#Ejercicio 1
nombre = input("Escribe tu nombre: ")
apellido = input("Escribe tu apellido: ")

#Convertimos a minúsculas y unimos nombre y apellido sin espacios
nombre_usuario = (nombre+apellido).lower()

# Generamos un número aleatorio para añadirlo al nombre de usuario
numero= random.randint(10,99)

# Concatenamos todo
usuario_final = f"{nombre_usuario}{numero}"
print(f"tu nombre de usuario es: {usuario_final}")

#EJERCICIO 2
frase = input("introduce una frase")

print("longitud de la frase",len(frase))
print("¿contiene python?","python" in frase)
print("Frase en mayusculas", frase.upper())
print("Frase invertida",frase[::-1])

#EJERCICIO 3
precio = float(input("escribe el precio del producto"))

#se calcula descuento y nuevo precio
descuento = precio * 0.15
precio_final = precio-descuento

print(f"precio con descuento: €{precio_final:.2f}" )
print(f"Redondeado hacia arriba: €{math.ceil(precio_final)}")

#EJERCICIO 4
producto = input("Nombre de producto: ")
Precio =float(input("Precio del producto: "))

etiqueta_producto = f"PRODUCTO:{producto.upper()}- PRECIO:  {Precio:.2F}€-CODIGO:{ord(producto[0])}"

print(etiqueta_producto)

#EJERCICIO 5
numeros = input("Escribe números separados por comas: ")

# Convertimos en lista, eliminamos duplicados y ordenamos
lista_numeros = list(set(map(int, numeros.split(","))))

print("Lista sin duplicados y ordenada:", sorted(lista_numeros))

#EJERCICIO 6
nombre = input("Escribe tu nombre: ")

# Generamos una contraseña aleatoria
contraseña = f"{nombre[0].upper()}-{random.randint(100, 999)}-*"

print(f"Tu nueva contraseña es: {contraseña}")

