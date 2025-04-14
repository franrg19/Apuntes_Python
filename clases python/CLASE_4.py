




#EJERCICIO 4: INDICES Y SUBCADENAS
#Define una cadena extensa (minimo 50 caracteres)
#obten varias subcadenas usando la indexacion por rangos (slicing) y genera
#una nueva cadena combinando estas subcadenas en orden inverso
#imprime la nueva cadena resultante

# cadena_extensa ="python es un super lenguaje que me re encanta"
# subcadena= cadena_extensa[0:6] + "" + cadena_extensa[11:20]
# resultado=subcadena[::-1]
# print(resultado)

#EJERCICIO 5:FORMATO Y CONVERSION NUMERICA
#DEFINE VARIABLES NUMERICAS (ENTERO,FLOTANTE,COMPLEJO)
#CREA UNA CADENA CON FORMATO AVANZADO (F-STRINGS) QUE MEUSTRE ESTOS NUMEROS
#CON PRECISION DEFINIDA (DOS DECIMALES, NOTACION CIENTIFCA,ETC.)
#EVITA CONCATENAR DIRECTAMENTE NUMEROS Y TEXTO

# entero,flotante,complejo = 12, 345.23976,5+3j
# formato = f"Entero:{entero}, Flotante{flotante:.2f},notacion cientifica:{flotante:.2e},complejo{complejo}"
# print(formato)

#EJERCICIO6: OPERACIONES COMBINADAS entre numeros y cadenas
#define dos variables numericas enteras y dos cadenas
#realiza calculos matematicos diversos y genera una cadena formateada
#que explique cada operacions(suma,restas,multiplicaciones,modulo)
#claramente utilizando metodos de cadenas
# num_a, num_b = 15 ,4
# cad_a, cad_b = "la multiplicacion da: " , "y el resto des: "
# resultado = f"{cad_a}{num_a * num_b}, {cad_b}{num_a%num_b}"
# print(resultado)

#EJERCICIO 7 CALCULO DEL AREA Y PERIMETRO
#DEFINE VARIABLES NUMERICAS QUYE REPRESENTE DIMENSIAONES (LARGO , AMNCHO ,RADIOM ALTURA)
#CALCULA EL AREA Y PERIMETRO DE DISTINTAS FUGUTRAS GEOMETRICAS
#(RECTANGULO,CIRCULO,TRIANGULO RECTANGULO)
#PRESENTA TODOS LOS RESULTADOS CLARAMENTE EN UNSA SOLA CADENA FORMATEADA USANDO CONVERSIONES EXPLICITAS

largo,ancho,radio,altura = 10,5,3,4
area_rectangulo = largo*ancho
perimetro_rectangulo = 2*(largo*ancho)
area_circulo = 3.14 * radio **2
perimetro_circulo = 2*3.14*radio
area_triangulo = (largo*altura)*2
resultado =(f"area de un rectangulo: {area_rectangulo},"
            f"Perimetro del rectangulo: {perimetro_rectangulo},")
