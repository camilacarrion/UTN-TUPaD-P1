# EJERCICIOS_TRABAJO_PRACTICO_3

# EJERICIO 1: Mayor de edad
# edad = int(input("Por favor ingrese su edad: "))
# if edad >= 18:
#     print ("Usted es mayor de edad")
# else:
#     print ("Usted es menor de edad")

# EJERCICIO 2: Aprobado/Desaprobado
# nota = int(input("Por favor ingrese su nota: "))
# if nota >= 6:
#     print ("Felicitaciones! Usted aprobo la asignatura!")
# else:
#     print ("Usted NO aprobo la asignatura!")

# EJERCICIO 3: Par/Impar
# numero = int(input("Por favor ingrese un numero: "))
# if numero % 2 == 0:
#     print ("Ha ingresado un número par!")
# else:
#     numero = int(input("Por favor, ingrese un número par! "))

# EJERCICIO 4: Edad del usuario
# edad = int(input("Por favor ingrese su edad: "))
# if edad < 12:
#     print("Usted es un niño/a!")
# elif edad == 12 or edad < 18:
#     print("Usted es un adolescente!")
# elif edad >= 18 and edad < 30:
#     print("Usted es un adulto/a joven!")
# else:
#     print("Usted es un adulto!")

# EJERCICIO 5: Contraseña
# clave = input("Por favor ingrese una contaseña, debe tener entre 8 y 14 caracteres!: ")
# digitos = len(clave)
# if digitos >= 8 and digitos <= 14:
#     print ("Ha ingresado una contraseña correcta")
# else:
#     print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# EJERCICIO 6: Parametros estadisticos
# import random
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# from statistics import mode,median,mean
# moda = mode (numeros_aleatorios)
# mediana = median (numeros_aleatorios)
# media = mean (numeros_aleatorios)
# print ("La media es: ",media," La mediana es: ",mediana," La moda es: ",moda)
# if media > mediana and mediana > moda:
#     print ("Hay sesgo positivo, o hacia la derecha")
# elif media < mediana and mediana < moda:
#     print ("Hay sesgo negativo, o hacia la izquierda")
# elif media == moda == mediana:
#     print ("No hay sesgo")
# else: 
#     print("Los valores no entran dentro de ninguna clasificacion")

# EJERCICIO 7: Palabra terminada en vocal
# palabra = input ("Por favor ingrese una palabra: ")
# ultima_letra = palabra[-1]
# if ultima_letra in "aeiou":
#     print(f"{palabra}!")
# else:
#     print (palabra)

# EJERCICIO 8: Nombre es may/min
# nombre = input("por favor ingrese su nombre: ")
# print ("1: Nombre en mayuscula")
# print ("2: Nombre en minuscula")
# print ("3: Primera letra en mayuscula y el resto en minuscula")
# opcion = input("Ingrese la opcion elegida: ")
# if opcion == "1":
#     print (nombre.upper())
# elif opcion == "2":
#     print (nombre.lower())
# elif opcion == "3":
#     print (nombre.title())

# EJERCICIO 9: Magnitud de terremoto
# magnitud = float(input("Ingrese la magnitud del terremoto: "))
# if magnitud < 3:
#     print ("El terremoto fue muy leve (imperceptible)")
# elif magnitud >= 3 and magnitud < 4:
#     print ("El terremoto fue leve (ligeramente perceptible)")
# elif magnitud >= 4 and magnitud < 5:
#     print ("El terremoto fue moderado (sentido por personas, pero generalmente no causa daños)")
# elif magnitud >= 5 and magnitud < 6:
#     print ("El terremoto fue fuerte (puede causar daños en estructuras débiles)")
# elif magnitud >= 6 and magnitud < 7:
#     print ("El terremoto fue muy fuerte (puede causar daños significativos)")
# elif magnitud >= 7:
#     print ("El terremoto fue extremo (puede causar graves daños a gran escala)")

# EJERCICIO 10: Estaciones del año
# hemisferio = input("Por favor ingrese S si se encuentra en el hemisferio Sur, o N si se encuentra en el hemisferio Norte: ").upper()
# mes = int(input("Por favor ingrese el número del mes (1 al 12): "))
# dia = int(input("Por favor ingrese el día: "))
# if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
#     estacion = "Verano" if hemisferio == "S" else "Invierno"
# elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
#     estacion = "Otoño" if hemisferio == "S" else "Primavera"
# elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
#     estacion = "Invierno" if hemisferio == "S" else "Verano"
# elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
#     estacion = "Primavera" if hemisferio == "S" else "Otoño"
# else:
#     estacion = "Fecha inválida"
# print(f"La estación en el hemisferio {hemisferio} es: {estacion}")



