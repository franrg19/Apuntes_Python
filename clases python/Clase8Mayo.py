'''
Ejercicio 9 - Suma acumulativa¶
Escribe un programa que pida al usuario una serie de números enteros y calcule la suma acumulativa de esos números.
El programa debe seguir pidiendo números hasta que el usuario ingrese un 0. Al final, imprime la suma total.
'''

print("Introduce numeros para sumarlos y para acabar introduce 0")
numero = int(input())
resultado =0

while numero != 0:
    resultado+=numero
    numero = int(input())

print(f"El resultado es {resultado}")



'''
Ejercicio 10 - Akinator numérico¶
Escribe un programa que escoja un número aleatorio entre 1 y 100 y le pida al usuario que adivine el número. 
El programa debe dar pistas al usuario si el número es mayor o menor que el número elegido. 
El programa debe seguir pidiendo números hasta que el usuario adivine el número correcto.
'''

import random
from sys import hash_info

numero_aleatorio = random.randint (1,100)

numero_usuario= int(input("introduce un numero del 1 al 100: "))

while numero_aleatorio != numero_usuario:
    if numero_usuario > numero_aleatorio:
        print("Lo siente es demasiado alto")
    else:
        print("casiiii")

    numero_usuario= int(input("introduce un numero del 1 al 100: "))

print("Enhorabuena lo has adivinado")


'''
Ejercicio 12 - Mayor y menor¶
Escribe un programa que pida al usuario una serie de números enteros y determine cuál es el mayor y cuál es el menor. 
El programa debe seguir pidiendo números hasta que el usuario ingrese un 0. Al final, imprime el mayor y el menor.
'''

mayor = -hash_info.inf
menor = hash_info.inf
numero = int(input("introduce un valor (0 para terminar)"))


while numero !=0:
    if numero > mayor:
        mayor =numero
    if numero < menor:
        menor = numero
    numero = int(input("introduce un valor (0 para terminar)"))

print(f"Mayor: {mayor} Menor: {menor}")


'''
Ejercicio 13 - Número de cifras¶
Escribe un programa que pida al usuario una serie de números enteros positivos hasta la introducción de un valor -1 para cada número debe contar cuántas cifras tiene. 
El programa debe imprimir la longitud de cada número.
 No podéis usar la función len() para contar las cifras ni convertir el número a cadena.
'''

numero = int(input("Introduce un numero (-1 para acabar):"))


while numero != -1:
    cifras = 1
    copia_num= numero
    while numero >9:
        cifras+=1
        numero //=10
    print(f"el numero de digitos de {copia_num} es {cifras} ")

    numero = int(input("Introduce un numero (-1 para acabar):"))


'''
Escribe un programa que simule una cuenta bancaria. El programa debe permitir al usuario realizar las siguientes operaciones:

1.Ingresar dinero
2.Retirar dinero
3.Consultar saldo
4.Salir
Inicializa el saldo en 0 y permite al usuario realizar operaciones hasta que decida salir.
'''

saldo = 0
opcion = -1

while opcion != 4:
    print("Escoge una opcion: ")
    print("1. Ingresar dinero")
    print("2. Retirar saldo ")
    print("3. Consultar saldo")
    print("4. Salir ")

    opcion = int(input())

    if opcion == 1:
        saldo += int(input("¿Cuanto quieres ingresar?"))
    elif opcion == 2:
        saldo -= int(input("¿Cuanto quieres retirar?"))
    elif opcion == 3:
        print(f"El saldo es de {saldo}")
    else:
        print("Escoge una opcion del menu")
