import random

# -----------------------------------------------------------------------------------
# Ejercicio 1

notas = [10, 8, 7, 10, 6, 5, 7, 3, 9]

# Mostrar las notas de los alumnos
for i, nota in enumerate(notas):
    print(f"Estudiante {i + 1}: {nota}")
print("-" * 20)

# Calcular y mostrar el promedio
suma = 0
for nota in notas:
    suma += nota
promedio = suma / len(notas)
print("Promedio de las notas:", round(promedio, 2))
print("-" * 20)

# Mostrar la nota mayor y baja
mayor = notas[0]
menor = notas[0]

for nota in notas:
    if nota > mayor:
        mayor = nota
    if nota < menor:
        menor = nota

print("Nota más alta:", mayor)
print("Nota más baja:", menor)
print("-" * 20)

# -----------------------------------------------------------------------------------
# Ejercicio 2

lista_productos = []

# Pedir que el usuario cargue 5 productos
for i in range(0, 5):
    print(f"Ingrese el producto {i + 1}:")
    producto = input("> ")
    lista_productos.append(producto)
print("-" * 20)

# Mostrar lista ordenada
print("LISTA ORDENADA POR ORDEN ALFABETICO:")
lista_productos_ordenada = sorted(lista_productos)
for i in range(0, len(lista_productos_ordenada)):
    print(f"Producto {i + 1}: {lista_productos_ordenada[i]}")
print("-" * 20)

print("Indique qué producto desea eliminar")
while True:
    producto_eliminar = input("> ")  # pedir dentro del bucle
    
    if producto_eliminar not in lista_productos_ordenada:
        print("Error, el producto no está en la lista. Intente de nuevo:")
        continue
    else:
        print(f"El producto {producto_eliminar} ha sido eliminado")
        lista_productos_ordenada.remove(producto_eliminar)
        break
print("-" * 20)

print("Lista nueva: ")
for i in range(0, len(lista_productos_ordenada)):
    print(f"Producto {i + 1}: {lista_productos_ordenada[i]}")
print("-" * 20)

# -----------------------------------------------------------------------------------
# Ejercicio 3

# Generar una lista con 15 números enteros al azar entre 1 y 100.
lista_numeros = []

for i in range(0, 15):
    numero_azar = random.randint(0, 100)
    lista_numeros.append(numero_azar)

# Crear una lista con los pares y otra con los impares.
lista_pares = []
lista_impares = []

for num in lista_numeros:
    if num % 2 == 0:
        print(f"El numero {num} es par")
        lista_pares.append(num)
    else: 
        print(f"El numero {num} es impar")
        lista_impares.append(num)
print("-" * 20)

print("Los numeros pares son: ")
for num in lista_pares:
    print(f"> {num}")
print(f"Hay un total de: {len(lista_pares)}")
print("-" * 20)

print("Los numeros impares son: ")
for num in lista_impares:
    print(f"> {num}")
print(f"Hay un total de: {len(lista_impares)}")
print("-" * 20)

# -----------------------------------------------------------------------------------
# Ejercicio 4

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
sin_repetir = []

# Crear una nueva lista sin elementos repetidos.
for num in datos:
    if num not in sin_repetir:
        sin_repetir.append(num)

# Mostrar el resultado.
for num in sin_repetir:
    print(num, end=" ")

# -----------------------------------------------------------------------------------
# Ejercicio 5

list_estudiantes = []

print("Ingrese la lista de 8 estudiantes asistentes")
for i in range(0, 8):
    print(f"Estudiante {i + 1}")
    estudiante = input("> ")
    list_estudiantes.append(estudiante)
print("-" * 20)

print("Seleccione la opcion que desea: ")
while True:
    print("(1) Agregar nuevo estudiante")
    print("(2) Eliminar estudiante existente")
    print("(3) Salir del menu")
    opcion = int(input("> "))

    if opcion == 1:
        print("Ingrese el estudiante a ingresar: ")
        estudiante_add = input("> ")
        list_estudiantes.append(estudiante_add)
        print(f"Estudiante {estudiante_add} agregado")
        continue
    if opcion == 2:
        while True:
            print("Ingrese el estudiante a eliminar: ")
            estudiante_remove = input("> ")
            if estudiante_remove not in list_estudiantes:
                print("Error, el estudiante no existe en la lista")
                continue
            else:
                print(f"Estudiante {estudiante_remove} ha sido eliminado")
                break
        continue
    if opcion == 3:
        break
print("-" * 20)

print("Lista final actualizada: ")
for i in range(0, len(list_estudiantes)):
    print(f"Estudiante {i + 1}: {list_estudiantes[i]}")

# -----------------------------------------------------------------------------------
# Ejercicio 6

lista_a_rotar = [10, 45, 62, 22, 35, 98, 7]
ultimo_numero = lista_a_rotar[-1]

for i in range(len(lista_a_rotar) - 1, 0, -1):
    lista_a_rotar[i] = lista_a_rotar[i - 1]

lista_a_rotar[0] = ultimo_numero

for num in range(0, len(lista_a_rotar)):
    print(f"{lista_a_rotar[num]}", end=" ")

# -----------------------------------------------------------------------------------
# Ejercicio 7

matriz_temps = [
    [20, 25],
    [22, 29],
    [19, 24],
    [24, 30],
    [22, 25],
    [20, 27],
    [20, 22]
]

dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"
               "Sabado", "Domingo"]

suma_minima = 0
suma_maxima = 0
cantidad_filas = len(matriz_temps)

for temps in matriz_temps:
    suma_minima += temps[0]
    suma_maxima += temps[1]

promedio_minima = round(suma_minima / cantidad_filas, 2)
promedio_maxima = round(suma_maxima / cantidad_filas, 2)
print(f"El promedio de la temperatura minima es: {promedio_minima}")
print(f"El promedio de la temperatura maxima es: {promedio_maxima}")
print("-" * 20)

temp_mas_fria = matriz_temps[0][0]
dia_mas_frio = 0
temp_mas_caluroso = matriz_temps[0][1]
dia_mas_caluroso = 0

for i, temp in enumerate(matriz_temps):
    if temp[0] < temp_mas_fria:
        temp_mas_fria = temp[0]
        dia_mas_frio = i
    
    if temp[1] > temp_mas_caluroso:
        temp_mas_caluroso = temp[1]
        dia_mas_caluroso = i

print(f"El dia mas frio fue: {dias_semana[dia_mas_frio]}")
print(f"Registrando una temperatura de: {temp_mas_fria}")
print("-" * 20)
print(f"El dia mas frio fue: {dias_semana[dia_mas_caluroso]}")
print(f"Registrando una temperatura de: {temp_mas_caluroso}")
print("-" * 20)

# -----------------------------------------------------------------------------------
# Ejercicio 8

matriz_estudiantes = [
    [10, 9, 10],
    [8, 9, 7],
    [10, 7, 7],
    [6, 9, 7],
    [10, 10, 10]
]

# Promedio de cada estudiante
for index, estudiante in enumerate(matriz_estudiantes):
    suma = 0
    for i in range(0, 3):
        suma += estudiante[i]
    print(f"Promedio de estudiante {index + 1}:")
    print(f"> {round(suma / len(estudiante), 2)}")
print("-" * 20)

# Promedio de cada materia
for i in range(0, 3):
    suma = 0
    for estudiante in matriz_estudiantes:
        suma += estudiante[i]
    print(f"Promedio materia {i + 1}:")
    print(f"> {suma / 5}")
    
print("-" * 20)

# -----------------------------------------------------------------------------------
# Ejercicio 9

def verificar_ganador(tablero):
    # Revisar filas
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] and fila[0] != "[ ]":
            return True

    # Revisar columnas
    for c in range(3):
        if tablero[0][c] == tablero[1][c] == tablero[2][c] and tablero[0][c] != "[ ]":
            return True

    # Revisar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != "[ ]":
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != "[ ]":
        return True

    return False


tablero = [
    ["[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]"]
]

jugador = 1
while True:
    print("🏁 ​El tablero actual 🏁")
    for row in tablero:
        print(row)
    print("-" * 20)
    print(f"🫵 ​ Jugador {jugador}, ingrese fila y columna (1 a 3):")
    while True:
        fila = int(input("Fila > "))
        columna = int(input("Columna > "))

        if (fila < 1 or fila > 3) or (columna < 1 or columna > 3):
            print("Error, por favor ingrese un numero mayor a 1 y menor a 3")
            continue
        elif tablero[fila - 1][columna - 1] == "[X]" or tablero[fila - 1][columna - 1] == "[O]":
            print("Error, ya hay una ficha en esta columna o fila, intente de nuevo")
            continue
        else:
            break
    print("-" * 20)
    if jugador == 1:
        tablero[fila - 1][columna - 1] = "[X]"
    else:
        tablero[fila - 1][columna - 1] = "[O]"

    if verificar_ganador(tablero):
        print("🏆 ¡Jugador", jugador, "ha ganado!")
        print("🏁 ​El tablero actual 🏁")
        for row in tablero:
            print(row)
        print("-" * 20)
        break  # salir del while principal
    
    jugador = 2 if jugador == 1 else 1

# -----------------------------------------------------------------------------------
# Ejercicio 10

total_ventas = [
    [350, 420, 500, 610, 720, 810, 900],   
    [280, 390, 410, 520, 680, 750, 820],   
    [600, 720, 810, 950, 870, 910, 1020],  
    [150, 200, 250, 300, 400, 500, 600]    
]

dias_ventas = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

print("Total de ventas por producto: ")
# Total de cada producto y el producto mas vendido de la semana:
producto_mas_vendido = 0
total_semana = 0
for index, ventas in enumerate(total_ventas):
    suma = 0
    for i in range(0, 7):
        suma += ventas[i]
    print(f"Producto {index + 1}: ${suma}")
    if suma > total_semana:
        producto_mas_vendido = index
        total_semana = suma
print(f"El producto mas vendido fue el producto {producto_mas_vendido + 1}")
print(f"Con un total de > ${total_semana}")
print("-" * 20)

print("Total de ventas por dia: ")
# Mostrar dia con mayor total:
dia_mas_venta = 0
total_mas_venta = 0

for i in range(0, 7):
    suma = 0
    for index in range(0, 4):
        suma += total_ventas[index][i]
    print(f"{dias_ventas[i]}: ${suma}")
    if suma > total_mas_venta:
        total_mas_venta = suma
        dia_mas_venta = i

print(f"El dia con mas venta fue: {dias_ventas[dia_mas_venta]}")
print(f"Con un total de > ${total_mas_venta}")
print("-" * 20)