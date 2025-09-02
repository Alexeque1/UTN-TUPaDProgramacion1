import random

# -----------------------------------------------------------------------------------
# Ejercicio 1

for i in range(0, 101):
    print(i)

# -----------------------------------------------------------------------------------
# Ejercicio 2

numero_usuario = int(input("Ingrese un numero entero: "))
print(f"Cantidad de digitos: {len(str(numero_usuario))}")

# -----------------------------------------------------------------------------------
# Ejercicio 3

numero_usuario_1 = int(input("Ingrese el primer numero: "))
numero_usuario_2 = int(input("Ingrese el primer numero: "))
suma_numeros = 0

for i in range(numero_usuario_1, numero_usuario_2 + 1):
    if i != numero_usuario_1 and i != numero_usuario_2:
        suma_numeros += i

print(f"""La suma de los numeros entre {numero_usuario_1} y {numero_usuario_2}
excluyendo ambos numeros es: {suma_numeros}""")

# -----------------------------------------------------------------------------------
# Ejercicio 4

total = 0

while True:
    numero_user = int(input("Ingrese un numero (O ingrese 0 si quiere terminar): "))
    if numero_user == 0:
        break
    total += numero_user

print(f"El total es: {total}")

# -----------------------------------------------------------------------------------
# Ejercicio 5

numero_aleatorio = random.randint(0, 9)
contador = 0

while True:
    contador += 1
    num_user = int(input("Ingrese un numero: "))

    if num_user == numero_aleatorio:
        print("¡Ganaste!")
        print(f"Lo hiciste en {contador} turnos")
        break
    else:
        print("Error, intentalo de nuevo")

# -----------------------------------------------------------------------------------
# Ejercicio 6

for i in range(100 - 2, 0, -2):
    print(i)

# -----------------------------------------------------------------------------------
# Ejercicio 7

num_positivo = int(input("Ingrese un numero positivo: "))
suma_nums = 0

while num_positivo < 0:
    num_positivo = int(input("Error, debe ingresar un numero positivo: "))

for i in range(0, num_positivo + 1):
    suma_nums += i

print(f"La suma de los numeros es: {suma_nums}")

# -----------------------------------------------------------------------------------
# Ejercicio 8

nums_positivos = 0
nums_negativos = 0
nums_pares = 0
nums_impares = 0

for i in range(1, 101):
    num_ingresado = int(input(f"{i}. Ingrese un numero: "))

    if num_ingresado > 0:
        nums_positivos += 1
    
    if num_ingresado < 0:
        nums_negativos += 1

    if num_ingresado % 2 == 0:
        nums_pares += 1
    else:
        nums_impares += 1

print(f"Numeros positivos: {nums_positivos}")
print(f"Numeros negativos: {nums_negativos}")
print(f"Numeros pares: {nums_pares}")
print(f"Numeros impares: {nums_impares}")

# -----------------------------------------------------------------------------------
# Ejercicio 9

suma_promedio = 0

for i in range(1, 101):
    num_ingresado = int(input(f"{i}. Ingrese un numero: "))

    suma_promedio += num_ingresado

print(f"El promedio de los numeros es: {suma_promedio / 100}")

# -----------------------------------------------------------------------------------
# Ejercicio 10

num_user_ingresado = input("Ingrese un numero: ")
num_invertido = "".join(reversed(num_user_ingresado))

print(f"El numero invertido es: {num_invertido}")