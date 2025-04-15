# TP4_ESTRUCTURAS_REPETITIVAS

# EJERCICIO 1
# for i in range(100,-1,-1):
#     print (i)

# EJERCICIO 2
# numero = input("Por favor ingrese un numero: ")
# long = len(numero)
# print (f"El numero ingresado tiene ",(long)," digitos")

# EJERCICIO 3
# num1 = int(input("Por favor ingrese el primer numero: "))
# num2 = int(input("Por favor ingrese el segundo numero: "))
# suma = 0
# inicio = num1 +1
# for i in range(inicio,num2):
#     suma += i
# print (f"El resultado de la suma es: ",(suma))

# EJERCICIO 4
# numeros = int(input("Por favor ingrese un numero: "))
# suma = 0
# while numeros != 0:
#     suma += numeros
#     numeros = int(input("Por favor ingrese un numero: "))
# print (f"El total acumulado es: ",suma)

# EJERCICIO 5
# import random
# adivina = random.randint(0,9)
# contador = 1
# numero = int(input("Ingrese un numero: "))
# while adivina != numero:
#     numero = int(input("Ingrese otro numero! "))
#     contador += 1
# print (f"Adivinaste en el intento: ",contador,"! El numero era ",numero)

#EJERCICIO 6
# for i in range(101,-1,-1):
#     if i % 2 == 0:
#         print (i)

# EJERCICIO 7
# suma = 0
# max = int(input("Por favor ingrese un numero: "))
# for i in range(0,max+1):
#     suma += i
# print ("El total acumulado hasta el numero ingresado es: ",suma)

# EJERCICIO 8
# contador = 1
# pares = 0
# impares = 0
# positivo = 0
# negativo = 0
# for i in range (0,100):
#     numeros = int(input(f"Por favor ingrese el {contador} numero: "))
#     contador += 1
#     if numeros % 2 == 0:
#         pares += 1
#     else:
#         impares += 1
#     if numeros >= 0:
#         positivo += 1
#     else:
#         negativo += 1
# print ("La cantidad de numeros pares es: ",pares)
# print ("La cantidad de numeros impares es: ",impares)
# print ("La cantidad de numeros positivos es: ",positivo)
# print ("La cantidad de numeros negativos es: ",negativo)

# EJERCICIO 9
# contador = 0
# suma = 0
# for i in range (0,100):
#     numeros = int(input("Por favor ingrese un numero: "))
#     suma += numeros
#     contador += 1
# print (f"El promedio es {suma/contador}")

# EJERCICIO 10
# numero = input("Por favor ingrese un numero: ")
# numero_invertido = numero[::-1]
# print("El numero invertido es:", numero_invertido)



