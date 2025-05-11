numero = int(input("Introduce un número entero positivo impar: "))

if numero > 0 and numero % 2 != 0:
    for fila in range(numero):
        for columna in range(numero):
            # Imprimimos 'x' en los bordes y en las diagonales
            if fila == 0 or fila == numero - 1 or columna == 0 or columna == numero - 1 or fila == columna or columna == numero - fila - 1:
                print("x", end="")
            else:
                print(" ", end="")  # Espacios en el interior para la cruz
        print()  # Salto de línea para la siguiente fila
else:
    print("Debe ser un número entero positivo impar.")
