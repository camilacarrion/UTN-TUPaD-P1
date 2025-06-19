# EJERCICIO 1:
# def factorial(n):
#  if n == 0 or n == 1:
#      return 1
#  else:
#     return n * factorial(n - 1)
 
# EJERCICIO 2:
# def fibonacci(n):
#  if n == 0:
#     return 0
#  elif n == 1:
#     return 1
#  else:
#     return fibonacci(n - 1) + fibonacci(n - 2)
 
# EJERCICIO 3:
# def pot(base, exponente):
#  if exponente == 0:
#     return 1
#  else:
#     return base * pot(base, exponente - 1)
 
# EJERCICIO 4:
# def decimal_binario(n):
#  if n == 0:
#     return ""
#  else:
#     return decimal_binario(n // 2) + str(n % 2)
 
# EJERCICIO 5:
# def palindromo(palabra):
#  if len(palabra) <= 1:
#     return True
#  if palabra[0] != palabra[-1]:
#     return False
#  return palindromo(palabra[1:-1])

# EJERCICIO 6:
# def suma(n):
#  if n < 10:
#     return n
#  else:
#     return n % 10 + suma(n // 10)
 
# EJERCICIO 7:
# def contar(n):
#  if n == 1:
#     return 1
#  else:
#     return n + contar(n - 1)
 
# EJERCICIO 8:
# def contar(numero, digito):
#  if numero == 0:
#     return 0
#  else:
#     ultimo = numero % 10
#     return (1 if ultimo == digito else 0) + contar(numero // 10, digito)
 
