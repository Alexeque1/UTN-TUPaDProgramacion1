# Ejercicio 1
def imprimir_hola_mundo():
    print("Hola, Mundo!")

imprimir_hola_mundo()


# Ejercicio 2
def saludar_usuario(nombre):
    print(f"¡Hola, {nombre}!")

print("Ingrese su nombre")
nombre = input("> ")
saludar_usuario(nombre)


# Ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

print("Ingrese su nombre")
user_name = input("> ")
print("Ingrese su apellido")
user_lastname = input("> ")
print("Ingrese su edad")
user_age = int(input("> "))
print("Ingrese su residencia")
user_residence = input("> ")

informacion_personal(user_name, user_lastname, user_age, user_residence)

# Ejercicio 4
def calcular_area_circulo(radio):
    return 3.1416 * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * 3.1416 * radio

print("Ingrese el radio del ciruclo")
radio_circle = float(input("> "))

print(f"El area del ciruclo es: {calcular_area_circulo(radio_circle)}")
print(f"El perimetro del circulo es: {calcular_perimetro_circulo(radio_circle)}")

# Ejercicio 5
def segundos_a_horas(segundos):
    return segundos / 3600

print("Ingrese los segundos")
segundos = int(input("> "))
print(f"Las horas son: {round(segundos_a_horas(segundos), 2)}")

# Ejercicio 6
def tabla_multiplicar(numero):
    for i in range(11):
        print(f"{numero} x {i} = {numero * i}")

print("Ingrese el numero para ver su tabla")
numero_multiplicar = int(input("> "))
tabla_multiplicar(numero_multiplicar)

# Ejercicio 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = 0
    if b == 0:
        division = "Error"
    else:
        division = a / b
    
    return (suma, resta, multiplicacion, division)

def mostrar_resultados(resultados, num1, num2):
    operaciones = ("suma", "resta", "multiplicacion", "division")
    for i, operacion in enumerate(operaciones):
        if resultados[i] != "Error":
            print(f"La {operacion} entre {num1} y {num2} da: {resultados[i]}")
        else:
            print("La división no es posible, no se puede dividir entre 0")

print("Ingrese numero 1:")
num1 = int(input("> "))
print("Ingrese numero 2:")
num2 = int(input("> "))
resultados = operaciones_basicas(num1, num2)

mostrar_resultados(resultados, num1, num2)

# Ejercicio 8
def calcular_imc(peso, altura):
    return round(peso / altura ** 2, 2)

print("Ingrese su peso")
user_weight = float(input("> "))
print("Ingrese su altura")
while True:
    user_height = input("> ")
    if "." not in user_height:
        print("Error, debe ingresar su altura con el siguiente formato: '1.70'")
        continue
    break

print(f"Su índice de masa corporal (IMC) es: {calcular_imc(user_weight, float(user_height))}")

# Ejercicio 9
def celsius_a_fahrenheit(celsius):
    return (celsius * (9 / 5)) + 32

print("Ingrese la temperatura en celsius °C")
temp_celsius = float(input("> "))
print(f"El equivalente en fahrenheit es: {celsius_a_fahrenheit(temp_celsius)}")

# Ejercicio 10
def calcular_promedio(a, b, c):
    suma = a + b + c
    return suma / 3

print("Ingrese numero 1")
num_prom_1 = int(input("> "))
print("Ingrese numero 2")
num_prom_2 = int(input("> "))
print("Ingrese su numero 3")
num_prom_3 = int(input("> "))

print(f"El promedio es: {calcular_promedio(num_prom_1, num_prom_2, num_prom_3)}")