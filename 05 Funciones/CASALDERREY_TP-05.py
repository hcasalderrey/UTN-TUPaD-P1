# Descriccion: Trabajo Práctico 5 - HERNAN CASALDERREY

import funciones_utiles #importando el módulo funciones_utiles

#1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal.

#Programa principal
funciones_utiles.imprimir_hola_mundo()

#2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario.

#Programa principal
nombre = input("Ingrese su nombre: ")
saludo = funciones_utiles.saludar_usuario(nombre)
print(saludo)

#3. Crear una función llamada informacion_personal(nombre, apellido,edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.


#Programa principal
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")

funciones_utiles.informacion_personal(nombre, apellido, edad, residencia)


#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
#calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.


#Programa principal
radio = float(input("Ingrese el radio del círculo: "))
print(f"El área del círculo es: {funciones_utiles.calcular_area_circulo(radio)}")
print(f"El perímetro del círculo es: {funciones_utiles.calcular_perimetro_circulo(radio)}")


#5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.


#Programa principal
segundos = int(input("Ingrese la cantidad de segundos: "))
horas, minutos = funciones_utiles.segundos_a_horas(segundos)
print(f"{segundos} segundos son {horas} horas y {minutos} minutos.")

#6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.


#Programa principal
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
funciones_utiles.tabla_multiplicar(numero)


#7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de 
#sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.



#Programa principal
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

suma, resta, multiplicacion, division = funciones_utiles.operaciones_basicas(a, b)
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")


#8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.


#Programa principal
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

imc = funciones_utiles.calcular_imc(peso, altura)
print(f"Su índice de masa corporal (IMC) es: {imc}")


#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.


#Programa principal
celsius = float(input("Ingrese la temperatura en Celsius: "))
fahrenheit = funciones_utiles.celsius_a_fahrenheit(celsius)
print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")


#10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta función.


#Programa principal
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))

promedio = funciones_utiles.calcular_promedio(a, b, c)
print(f"El promedio de los números es: {promedio}")
