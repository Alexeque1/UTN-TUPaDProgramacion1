# TRABAJO PRACTICO - ALEXANDER SEQUERA - Estructuras Secuenciales

# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola mundo")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.

print("-----------------------------")
nombre = input("Escriba su nombre: ")
print("-----------------------------")
print(f"Hola, {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.

print("-----------------------------")
nombreUsuario = input("Escriba su nombre: ")
apellidoUsuario = input("Escriba su apellido: ")
edadUsuario = input("Escriba su edad: ")
lugarUsuario = input("Escriba su lugar de residencia: ")
print("-----------------------------")
print(f"Soy {nombreUsuario} {apellidoUsuario}, tengo {edadUsuario} años y vivo en {lugarUsuario}.")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro

print("-----------------------------")
radioCirculo = float(input("Ingrese el radio de un circulo: "))
print("-----------------------------")
areaCirculo = 3.14159 * radioCirculo ** 2
perimetroCirculo = 2 * 3.14159 * radioCirculo
print("El área del círculo es:", areaCirculo)
print("El perímetro del círculo es:", perimetroCirculo)

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.

print("-----------------------------")
segundos = float(input("Ingrese una cantidad de segundos: "))
print("-----------------------------")
equivalenteHoras = segundos / 3600
print(f"{segundos} segundos equivale a {equivalenteHoras} horas")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.

print("-----------------------------")
numeroTabla = int(input("Ingrese un número del 1 al 10: "))
print("-----------------------------")
print(f"{numeroTabla} x 1 = {numeroTabla * 1}")
print(f"{numeroTabla} x 2 = {numeroTabla * 2}")
print(f"{numeroTabla} x 3 = {numeroTabla * 3}")
print(f"{numeroTabla} x 4 = {numeroTabla * 4}")
print(f"{numeroTabla} x 5 = {numeroTabla * 5}")
print(f"{numeroTabla} x 6 = {numeroTabla * 6}")
print(f"{numeroTabla} x 7 = {numeroTabla * 7}")
print(f"{numeroTabla} x 8 = {numeroTabla * 8}")
print(f"{numeroTabla} x 9 = {numeroTabla * 9}")
print(f"{numeroTabla} x 10 = {numeroTabla * 10}")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

print("-----------------------------")
primerNumero = int(input("Ingrese su primer número: "))
segundoNumero = int(input("Ingrese su segundo número: "))
print("-----------------------------")
print(f"Suma: {primerNumero} + {segundoNumero} = {primerNumero + segundoNumero}")
print(f"Resta: {primerNumero} - {segundoNumero} = {primerNumero - segundoNumero}")
print(f"Multiplicación: {primerNumero} * {segundoNumero} = {primerNumero * segundoNumero}")
print(f"División: {primerNumero} / {segundoNumero} = {primerNumero / segundoNumero}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
# modo:

print("-----------------------------")
alturaUsuario = float(input("Ingrese su altura: "))
pesoUsuario = float(input("Ingrese su peso: "))
print("-----------------------------")
print(f"Masa corporal: {pesoUsuario / alturaUsuario ** 2}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:

print("-----------------------------")
celsius = float(input("Ingrese una temperatura en celsius: "))
print("-----------------------------")
fahrenheit = (celsius * (9/5)) + 32
print(f"Temperatura en Fahrenheit: {fahrenheit}")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números
print("-----------------------------")
numPrimero = int(input("Ingrese el primer numero: "))
numSegundo = int(input("Ingrese el segundo numero: "))
numTercer = int(input("Ingrese el tercer numero: "))
print("-----------------------------")
promedio = (numPrimero + numSegundo + numTercer) / 3
print(f"El promedio de los tres números es: {promedio}")