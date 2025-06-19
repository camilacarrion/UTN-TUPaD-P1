# EJERCICIO 1:
# def imprimir_hola_mundo():
#     print("Hola Mundo!")
# imprimir_hola_mundo()

# EJERCICIO 2:
# def saludar(nombre):
#     return f"Hola {nombre}!"
# nombre = input("Ingrese su nombre: ")
# saludo = saludar(nombre)
# print(saludo)

# EJERCICIO 3:
# def datos_personales(nombre, apellido, edad, residencia):
#     print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
# nombre = input("Ingrese su nombre: ")
# apellido = input("Ingrese su apellido: ")
# edad = input("Ingrese su edad: ")
# residencia = input("Ingrese su lugar de residencia: ")
# datos_personales(nombre, apellido, edad, residencia)

# EJERCICIO 4:
# from math import pi
# def area_circulo(radio):
#     return pi*radio ** 2
# def perimetro_circulo(radio):
#     return 2 * pi * radio
# radio = float(input("Ingrese el radio del círculo: "))
# area = area_circulo(radio)
# perimetro = perimetro_circulo(radio)
# print(f"El área del círculo es: {area:.2f}")
# print(f"El perímetro del círculo es: {perimetro:.2f}")

# EJERCICIO 5:
# def seg_a_hs(segundos):
#     return segundos / 3600
# segundos = float(input("Ingrese los seg: "))
# horas = seg_a_hs(segundos)
# print(f"{segundos} seg equivalen a {horas:.2f} hs.")

# EJERCICIO 6:
# def tabla(numero):
#     print(f"Tabla de multiplicar de {numero}:")
#     for i in range(1, 11):
#         print(f"{numero} x {i} = {numero * i}")
# numero = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))
# tabla(numero)

# EJERCICIO 7:
# def operaciones(a, b):
#     suma = a + b
#     resta = a - b
#     multiplicacion = a * b
#     if b != 0:
#         division = a / b
#     else:
#         division = None
#     return (suma, resta, multiplicacion, division)
# a = float(input("Ingrese el primer número: "))
# b = float(input("Ingrese el segundo número: "))
# suma, resta, multiplicacion, division = operaciones(a, b)
# print("Suma:", suma)
# print("Resta:", resta)
# print("Multiplicación:", multiplicacion)
# if division is not None:
#     print("División:", division)
# else:
#     print("División: No se puede dividir por cero.")

# EJERCICIO 8:
# def imc(peso, altura):
#     return peso / (altura ** 2)
# peso = float(input("Ingrese su peso en kg: "))
# altura = float(input("Ingrese su altura en m: "))
# imc = imc(peso, altura)
# print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")

# EJERCICIO 9:
# def celsius_a_fahrenheit(celsius):
#     return (celsius * 9/5) + 32
# celsius = float(input("Ingrese la temperatura en grados Celsius: "))
# fahrenheit = celsius_a_fahrenheit(celsius)
# print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

# EJERCICIO 10:
# def promedio(a, b, c):
#     return (a + b + c) / 3
# num1 = float(input("Ingrese el primer número: "))
# num2 = float(input("Ingrese el segundo número: "))
# num3 = float(input("Ingrese el tercer número: "))
# promedio = promedio(num1, num2, num3)
# print(f"El promedio de {num1}, {num2} y {num3} es: {promedio:.2f}")
