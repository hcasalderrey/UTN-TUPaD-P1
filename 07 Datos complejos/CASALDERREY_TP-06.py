# Descriccion: Trabajo Práctico 6 - HERNAN CASALDERREY


#1) Dado el diccionario precios_frutas
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
#1450} Añadir las siguientes frutas con sus respectivos precios:
#● Naranja = 1200
#● Manzana = 1500
#● Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}
print(precios_frutas)
# Añadir las frutas y precios al diccionario
precios_frutas ['Naranja'] = 1200
precios_frutas ['Manzana'] = 1500
precios_frutas ['Pera'] = 2300
# Imprimir el diccionario actualizado 
print(precios_frutas)


##2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
##desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
##● Banana = 1330
##● Manzana = 1700
##● Melón = 2800

precios_frutas ['Banana'] = 1330
precios_frutas ['Manzana'] = 1700   
precios_frutas ['Melón'] = 2800
# Imprimir el diccionario actualizado
print(precios_frutas)

##3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
##desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
##precios.

print(precios_frutas.keys())


#4) Crear una clase llamada Persona que contenga un método __init__ con los atributos
#nombre, pais y edad y el método saludar. El método saludar debe imprimir por pantalla un
#mensaje de salud que siga la estructura "¡Hola! Soy [nombre], vivo en [pais] y tengo [edad]
#años."

class Persona:
    def __init__(self, nombre, pais, edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad

    def saludar(self):
        print(f"¡Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años.")

Ejemplo = Persona("Hernán", "Argentina", 41)
Ejemplo.saludar()


#5) Crear una clase llamada Circulo que contenga el atributo radio y los métodos calcular_area y
#calcular_perimetro. Dichos métodos deben calcular el parámetro correspondiente

import math
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

input_radio = float(input("Ingrese el radio del círculo: "))
FormaGeometrica = Circulo(input_radio) 
print(f"El área del circulo de radio {input_radio} es {FormaGeometrica.calcular_area()} y su perímetro es {FormaGeometrica.calcular_perimetro()}") 


#6) Dado un string con paréntesis "()", "{}", "[]", verifica si están correctamente balanceados usando una pila.

def verificar_balanceado(cadena):
       pila = []
       for char in cadena:
           if char in "({[":
               pila.append(char)
           elif char in ")}]":
               if not pila:
                   return False
               top = pila.pop()
               if char == ")" and top != "(":
                   return False
               elif char == "}" and top != "{":
                   return False
               elif char == "]" and top != "[":
                   return False
       return len(pila) == 0

programa = input("Ingrese una cadena de paréntesis: ")
resultado = verificar_balanceado(programa)
print("La cadena está balanceada." if resultado else "La cadena no está balanceada.")


#7) Usa una cola para simular un sistema de turnos en un banco. La cola debe permitir:
#● Agregar clientes (encolar).
#● Atender clientes (desencolar).
#● Mostrar el siguiente cliente en la fila.
 

class Cola:
    def __init__(self):
        self.cola = []

    def encolar(self, cliente):
        self.cola.append(cliente)

    def desencolar(self):
        if not self.cola:
            return None
        return self.cola.pop(0)

    def siguiente_cliente(self):
        if not self.cola:
            return None
        return self.cola[0]

Fila = Cola()
print("-----------------------------------------")
print( "Entran clientes a la fila.")
print("-----------------------------------------")

Fila.encolar("Cliente 1")
Fila.encolar("Cliente 2")
Fila.encolar("Cliente 3")
Fila.encolar("Cliente 4")

print("Clientes en la fila:", Fila.cola)
print("-----------------------------------------")

print("Siguiente cliente en la fila:", Fila.siguiente_cliente())
Fila.desencolar()
print("Cliente atendido.")
print("-----------------------------------------")

print("Siguiente cliente en la fila:", Fila.siguiente_cliente())
Fila.desencolar()
print("Cliente atendido.")
print("-----------------------------------------")

print("Siguiente cliente en la fila:", Fila.siguiente_cliente())
Fila.desencolar()
print("Cliente atendido.")
print("-----------------------------------------")

print("Clientes en la fila:", Fila.cola)
Fila.encolar("Cliente 5")
Fila.encolar("Cliente 6")
print("-----------------------------------------")
print("Entran más clientes a la fila.")
print("-----------------------------------------")


print("Clientes en la fila:", Fila.cola)

print("Siguiente cliente en la fila:", Fila.siguiente_cliente())
Fila.desencolar()
print("Cliente atendido.")
print("-----------------------------------------")
print("Clientes en la fila:", Fila.cola)

print("Siguiente cliente en la fila:", Fila.siguiente_cliente())
Fila.desencolar()
print("Cliente atendido.")
print("-----------------------------------------")
print("Siguiente cliente en la fila:", Fila.siguiente_cliente())
Fila.desencolar()
print("Cliente atendido.")
print("-----------------------------------------")
print("Clientes en la fila:", Fila.cola)


#8) Crea una lista enlazada que permita insertar nodos al inicio y recorrer la lista para mostrar
#los valores almacenados.

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
    

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def recorrer(self):
        nodo_actual = self.cabeza
        while nodo_actual:
            print(nodo_actual.valor, end=" -> ")	
            nodo_actual = nodo_actual.siguiente

Ejemplo = ListaEnlazada()
Ejemplo.insertar_inicio(1)
Ejemplo.insertar_inicio(2)
Ejemplo.insertar_inicio(3)
Ejemplo.insertar_inicio(4)
Ejemplo.insertar_inicio(5)


print("Valores en la lista enlazada:")
Ejemplo.recorrer() 

#9) Dada una lista enlazada, implementa una función para invertirla.

def invertir_lista_enlazada(lista):
    anterior = None
    actual = lista.cabeza
    while actual:
        siguiente = actual.siguiente
        actual.siguiente = anterior
        anterior = actual
        actual = siguiente
    lista.cabeza = anterior

invertir_lista_enlazada(Ejemplo)
print("\nLista enlazada invertida:")
Ejemplo.recorrer()
