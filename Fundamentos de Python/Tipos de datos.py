"""
    IMPRIMIR POR CONSOLA
"""
#print("Hola Mundo")
#print('Hola Mundo')

"""
    📌 Tipos de Datos Primitivos en Python
"""
# Enteros --------------------------------------------------------------------------------------------------------------------
edad = 25
temperatura = -3

#print(type(edad))  # <class 'int'>
#print(edad + temperatura)  # 22
#print(edad - temperatura)  # 28
#print(edad * temperatura)  # -75
#print(edad / temperatura)  # -8.333333333333334
#print(edad // temperatura)  # -9, esto devuelve la parte entera de la division
#print(edad % temperatura)  # 22, esto devuelve el residuo de la division


# Flotantes ----------------------------------------------------------------------------------------------------------------
altura = 1.75
peso = 70.5
pi = 3.1416
precio = 10.99

#print(type(altura))  # <class 'float'>

# Cadenas de texto ----------------------------------------------------------------------------------------------------------------
nombre = "Juan"
apellido = 'Pérez'
nombre_completo = nombre + " " + apellido + " tiene " + str(edad) + " años."

#print(type(nombre))  # <class 'str'>
#print(nombre_completo) 

# Booleanos ------------------------------------------------------------------------------------------------------------------
es_mayor_de_edad = True
es_estudiante = False

#print(True and False)
#print(True or False)
#print(not True)

"""
    📦 Tipos de Datos Estructurados
"""
# Listas --------------------------------------------------------------------------------------------------------------------
numeros = [1, 2, 3, 4, 5]
nombres = ["Juan", "María", "Pedro"]
numeros_mixtos = [1, 2.5, "tres", True]
    # Operaciones
#print(numeros[0])  # 1, accede al primer elemento de la lista
numeros.append(6)  # Agrega el número 6 al final de la lista
numeros.remove(2)  # Elimina el número 2 de la lista
nombres.remove("María")  # Elimina el nombre "María" de la lista
#print(len(nombres))  # 2, devuelve la longitud de la lista

# Tuplas --------------------------------------------------------------------------------------------------------------------
# Son similares a las listas, pero son inmutables (no se pueden modificar una vez creadas).
tupla = (1, 2, 3, 4, 5)
tupla_mixta = (1, 2.5, "tres", True)
    # Operaciones
#print(tupla_mixta)

# Conjuntos ------------------------------------------------------------------------------------------------------------
# Son colecciones no ordenadas de elementos únicos.
conjunto = {1, 2, 3, 4, 5}
conjunto_mixto = {1, 2.5, "tres", True}
    # Operaciones
#print(conjunto.add(6))  # Agrega el número 6 al conjunto
#print(conjunto.remove(2))  # Elimina el número 2 del conjunto
#print(conjunto)  # {1, 3, 4, 5, 6}
#print(conjunto.union({7, 8, 9}))  # Unión de conjuntos
conjunto.add(4) # No se agrega porque ya existe

# Diccionarios --------------------------------------------------------------------------------------------------------
# Son colecciones de pares clave-valor. Es como un objeto JSON.
# Se utilizan llaves {} para definir un diccionario y los pares clave-valor se separan por comas.
diccionario = {
    "nombre": "Juan",
    "edad": 25,
    "altura": 1.75,
    "es_estudiante": True
}
    # Operaciones
#print(diccionario["nombre"])  # "Juan", accede al valor asociado a la clave "nombre"
#print(diccionario["edad"])  # 25, accede al valor asociado a la clave "edad"
#print(diccionario.get("altura"))  # 1.75, accede al valor asociado a la clave "altura"
#print(diccionario.get("peso", "No existe"))  # "No existe", devuelve un valor por defecto si la clave no está presente
print(diccionario.keys())  # Devuelve las claves del diccionario
