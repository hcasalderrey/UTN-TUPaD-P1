import math

def imprimir_hola_mundo():
    print("Hola Mundo!")

def saludar_usuario(nombre):
    return f"Hola {nombre}!"


def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")


def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

def segundos_a_horas(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    return horas, minutos

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Error: División por cero"
    return suma, resta, multiplicacion, division

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return round(imc, 2)

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return round(fahrenheit, 2)

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return round(promedio, 2)