# Descriccion: Trabajo Práctico 4 - HERNAN CASALDERREY
#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
    print(i)


#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

num = int(input("Ingrese un número entero: "))
cont = 0
while num > 0:
    num = num // 10
    cont += 1
print("La cantidad de dígitos es:", cont)


#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
suma = 0
if num1 < num2:
    for i in range(num1 + 1, num2):
        suma += i
else:
    for i in range(num2 + 1, num1):
        suma += i

print("La suma de los números enteros entre", num1, "y", num2, "es:", suma)


#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.
 
num = int(input("Ingrese un número entero (0 para salir): "))
suma = 0
while num != 0:
    suma += num
    num = int(input("Ingrese otro número entero (0 para salir): "))
print("La suma total es:", suma)


#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
intentos = 0
numero_aleatorio = random.randint(0, 9)
numero_usuario = int(input("Adivina el número entre 0 y 9: "))
while numero_usuario != numero_aleatorio:
    intentos += 1
    if numero_usuario < numero_aleatorio:
        print("El número es mayor.")
    else:
        print("El número es menor.")
    numero_usuario = int(input("Adivina el número entre 0 y 9: "))
 
print("¡Felicidades! Adivinaste el número", numero_aleatorio, "en", intentos, "intentos.")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

num = int(input("Ingrese un número entero positivo: "))
suma = 0    
if( num % 2 == 0):
    for i in range(num + 1):
        suma += i
    print("La suma de los números enteros desde 0 hasta", num, "es:", suma)

else: 
    print("El número ingresado no es positivo.")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

num_pares = 0
num_impares = 0
num_positivos = 0
num_negativos = 0
for i in range(100):
    num = int(input("Ingrese un número entero: "))
    if num % 2 == 0:
        num_pares += 1
    else:
        num_impares += 1
    if num > 0:
        num_positivos += 1
    elif num < 0:
        num_negativos += 1

print("Cantidad de números pares:", num_pares)
print("Cantidad de números impares:", num_impares)
print("Cantidad de números positivos:", num_positivos)
print("Cantidad de números negativos:", num_negativos)


#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

suma =0 
for i in range(100):
    num = int(input("Ingrese un número entero: "))
    suma += num
media = suma / 100




#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num = int(input("Ingrese un número entero: "))
invertido = 0
while num > 0:
    digito = num % 10
    invertido = invertido * 10 + digito
    num = num // 10
print("El número invertido es:", invertido)

