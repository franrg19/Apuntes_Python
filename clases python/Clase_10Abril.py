#Ejercicio 1 - Siempre negatifo, nunca positifo

# numero = int(input ("introduce un numero entero: "))
# print(numero)

# # Comprobar si numero es positivo

# if numero >= 0:
#     print("positivo")
# else:
#     print("negativo")

#2. Portero Discoteca

# edad = int(input("¿Cuantos años tienes?"))

# if edad >= 18 and edad <= 60:
#     print ("puedes entrar")
# elif edad > 60:
#     print("vete a Oldschool")
# elif edad >=16:
#     print("vete a kindergarden")
# else:
#     print("Vete a tu casa")


# 3. PACMAN

# Pos_pacman = int(input("¿Cual es la posicion de Pacman?"))
# Pos_fantasma = int(input("¿Cual es la posicion del fantasma?"))

# if Pos_fantasma == Pos_fantasma:
#     # Caramelo -> Pacman come fantasma
#     #Invisible -> Pacman Escapa
#     #Normal -> Pacman atrapado

#     estado_pacman = input("¿Como esta pacman?")
#     if estado_pacman == "caramelo":
#         print("Pacman se ha comido al fantasma")
#     else:
#         print("Pacman fue atrapado")

# else:
#     print("Pacman ha escapado")


#4. Multiplos de 3 y 5

# # Pedimos un número al usuario
# numero = int(input("Introduce un número: "))

# # Comprobamos si es múltiplo de 3, 5, ambos o ninguno
# if numero % 3 == 0 and numero % 5 == 0:
#     print(f"{numero} es múltiplo de 3 y de 5.")
# elif numero % 3 == 0:
#     print(f"{numero} es múltiplo de 3.")
# elif numero % 5 == 0:
#     print(f"{numero} es múltiplo de 5.")
# else:
#     print(f"{numero} no es múltiplo ni de 3 ni de 5.")



#5.Puede entrar al servidor de Discord?

rol = input("¿cual es tu rol?").lower ()
academia = input("¿cual es tu academia?").lower ()

if rol == "alumno" and academia == "prometeo":
    print("tienes acceso al Discord oficial y de prometeo")
elif rol == "profesor" and academia == "Prometeo":
    print("Tienes acceso al discord oficial")
else:
    print("No tienes acceso al servidor de discord")

