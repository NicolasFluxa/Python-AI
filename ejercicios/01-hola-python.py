"""
Ejercicio 1: Hola Python!
Nivel: Básico

Objetivo: Familiarizarte con la sintaxis básica de Python
"""

# TODO: Completa los siguientes ejercicios

# Ejercicio 1.1: Variables y tipos de datos
print("=" * 50)
print("Ejercicio 1.1: Variables y tipos de datos")
print("=" * 50)

# TODO: Crea una variable con tu nombre
nombre = "Tu Nombre"

# TODO: Crea una variable con tu edad
edad = 0

# TODO: Crea una variable que indique si te gusta Python (True/False)
me_gusta_python = True

# TODO: Imprime un mensaje de presentación usando las variables
print(f"Hola, me llamo {nombre}, tengo {edad} años y me gusta Python: {me_gusta_python}")


# Ejercicio 1.2: Operaciones matemáticas
print("\n" + "=" * 50)
print("Ejercicio 1.2: Operaciones matemáticas")
print("=" * 50)

# TODO: Calcula el área de un rectángulo (base * altura)
base = 10
altura = 5
area_rectangulo = 0  # TODO: Completa la operación
print(f"Área del rectángulo: {area_rectangulo}")

# TODO: Calcula el promedio de tres números
num1, num2, num3 = 10, 20, 30
promedio = 0  # TODO: Completa la operación
print(f"Promedio de {num1}, {num2}, {num3}: {promedio}")


# Ejercicio 1.3: Listas
print("\n" + "=" * 50)
print("Ejercicio 1.3: Trabajando con listas")
print("=" * 50)

# TODO: Crea una lista con tus 5 lenguajes de programación favoritos
lenguajes = []  # TODO: Agrega los lenguajes

print(f"Mis lenguajes favoritos: {lenguajes}")

# TODO: Agrega un nuevo lenguaje a la lista
# lenguajes.append("...")

# TODO: Imprime el primer lenguaje de la lista
print(f"Mi lenguaje favorito es: {lenguajes[0] if lenguajes else 'ninguno'}")


# Ejercicio 1.4: Diccionarios
print("\n" + "=" * 50)
print("Ejercicio 1.4: Trabajando con diccionarios")
print("=" * 50)

# TODO: Crea un diccionario con información sobre ti
mi_info = {
    "nombre": "",
    "edad": 0,
    "ciudad": "",
    "lenguaje_favorito": ""
}

print(f"Mi información: {mi_info}")


# Ejercicio 1.5: Condicionales
print("\n" + "=" * 50)
print("Ejercicio 1.5: Condicionales")
print("=" * 50)

# TODO: Escribe un programa que determine si un número es par o impar
numero = 42
# TODO: Completa el condicional
if numero % 2 == 0:
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")


# Ejercicio 1.6: Bucles
print("\n" + "=" * 50)
print("Ejercicio 1.6: Bucles")
print("=" * 50)

# TODO: Imprime los números del 1 al 10
print("Números del 1 al 10:")
# for i in range(...):
#     print(i)

# TODO: Suma todos los números del 1 al 100
suma = 0
# TODO: Completa el bucle
print(f"Suma de números del 1 al 100: {suma}")


# Ejercicio 1.7: Funciones
print("\n" + "=" * 50)
print("Ejercicio 1.7: Funciones")
print("=" * 50)

# TODO: Crea una función que salude a una persona
def saludar(nombre):
    """Saluda a una persona"""
    # TODO: Completa la función
    pass

# TODO: Crea una función que calcule el cuadrado de un número
def cuadrado(numero):
    """Calcula el cuadrado de un número"""
    # TODO: Completa la función
    return 0

# Prueba tus funciones
# saludar("Python")
# print(f"El cuadrado de 5 es: {cuadrado(5)}")


# ¡Felicidades! Has completado el ejercicio básico de Python
print("\n" + "=" * 50)
print("🎉 ¡Felicidades! Has completado los ejercicios básicos")
print("=" * 50)
print("\n💡 Próximos pasos:")
print("   1. Ejecuta este archivo y verifica los resultados")
print("   2. Experimenta modificando los valores")
print("   3. Crea tus propias variaciones de los ejercicios")
print("   4. Continúa con el siguiente ejercicio")
