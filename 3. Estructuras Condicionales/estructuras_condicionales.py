
from statistics import mode, median, mean
import random

# -----------------------------------------------------------------------------------
# Ejercicio 1

edad = int(input("Ingrese su edad: "))  # Se le pide la edad al usuario

if edad >= 18:  # Si edad es mayor a 18, se imprime "mayor de edad"
    print("Usted es mayor de edad")

# -----------------------------------------------------------------------------------
# Ejercicio 2

nota_usuario = int(input("Ingrese su nota: "))

if nota_usuario >= 6:  # Si nota es >= 6, aprueba
    print("Usted esta aprobado")
else:  # Si nota es < 6, desaprueba
    print("Usted esta desaprobado")

# -----------------------------------------------------------------------------------
# Ejercicio 3

numero_usuario = int(input("Ingrese un numero: "))  # Se pide numero

# Si numero es par, se imprime mensaje
if numero_usuario % 2 == 0: 
    print("Ha ingresado un numero par")
# Si no es par, se pide un numero par
else:
    print("Por favor, ingrese un numero par")

# -----------------------------------------------------------------------------------
# Ejercicio 4

edad_usuario = int(input("Ingrese su edad: "))

# Si edad es < 12, imprimir niño
if edad_usuario < 12: 
    print("Usted es un niño")
# Si edad es < 12, imprimir adolescente
elif edad_usuario >= 12 and edad_usuario < 18:
    print("Usted es un adolescente")
# Si edad es < 12, imprimir adulto joven
elif edad_usuario >= 18 and edad_usuario < 30:
    print("Usted es un adulto joven")
# Si edad es < 12, imprimir adulto adulto
elif edad_usuario >= 30:
    print("Usted es un adulto")

# -----------------------------------------------------------------------------------
# Ejercicio 5

password_usuario = input("Ingrese su contraseña: ")
password_long = len(password_usuario)

if password_long > 8 and password_long < 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# -----------------------------------------------------------------------------------
# Ejercicio 6

# Generar lista de numeros y mostrarlos
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
print("Lista de numeros: ", numeros_aleatorios)

# Seleccionar la moda, mediana y media y mostrarlos
numero_moda = mode(numeros_aleatorios)
numero_mediana = median(numeros_aleatorios)
numero_media = mean(numeros_aleatorios)
print("Moda:", numero_moda)
print("Mediana:", numero_mediana)
print("Media:", numero_media)

# En caso que media es mayor a mediana y a su vez mediana mayor a moda:
if numero_media > numero_mediana > numero_moda:
    print("Sesgo positivo o a la derecha")
# En caso que media es menor a mediana y a su vez mediana menor a moda:
elif numero_media < numero_mediana < numero_moda:
    print("Sesgo negativo o a la izquierda")
# En caso que media es igual a mediana y a su vez mediana igual a moda:
elif numero_media == numero_mediana == numero_moda:
    print("Sin sesgo")

# -----------------------------------------------------------------------------------
# Ejercicio 7

# Se pide la frase al usuario
frase_usuario = input("Ingresar una frase: ")
# Se toma la ultima letra y la volvemos minusculas para comparar
ultima_letra = frase_usuario[-1].lower()

# Comparamos la ultima letra con las vocales
# En caso de terminar con vocal, se agrega "!"
if ultima_letra in 'aeiou':
    frase_usuario += "!"

print("Frase resultante: ", frase_usuario)

# -----------------------------------------------------------------------------------
# Ejercicio 8

# Se pide el nombre del usuario
nombre_usuario = input("Ingrese su nombre: ")
# Pedimos que ingrese la opcion que desee
numero_user = int(input("Ahora, puede elegir entre estas opciones:\n"
                        "(1) Si quiere su nombre en mayúsculas\n"
                        "(2) Si quiere su nombre en minúsculas\n"
                        "(3) Si quiere su nombre con la primera letra mayúscula\n"
                        ""))

# Si selecciona 1, colocamos en mayusculas
if numero_user == 1:
    print(nombre_usuario.upper())
# Si selecciona 2, colocamos en minisculas
elif numero_user == 2:
    print(nombre_usuario.lower())
# Si selecciona 3, colocamos la primera letra en mayusculas
else:
    print(nombre_usuario.title())

# -----------------------------------------------------------------------------------
# Ejercicio 9

# Pedimos al usuario la magnitud del terremoto
magnitud = float(input("Ingrese la magnitud del terremoto: "))

# Se compara la magnitud ingresada por el usuario con el nivel
# Se evalua si es muy leve, leve, moderado, fuerte, muy fuerte o extremo
if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
elif magnitud >= 7:
    print("Extremo (puede causar graves daños a gran escala)")

# -----------------------------------------------------------------------------------
# Ejercicio 10

# Se pide el hemisferio al usuario
hemisferio_user = input("Ingrese el hemisferio donde se encuentra (Norte o Sur): ").lower()
# Se pide el mes
mes_user = int(input("Ingrese el mes (1 al 12): "))
# Se pide el dia
dia_user = int(input("Ingrese el dia (1 al 31): "))

# Validar entrada
if hemisferio_user not in ["norte", "sur"] or not (1 <= mes_user <= 12) or not (1 <= dia_user <= 31):
    print("Por favor, ingresar un hemisferio, mes o dia correcto")
else:  # Hemisferio norte
    if hemisferio_user == "norte":
        if (mes_user == 12 and dia_user >= 21) or (mes_user in [1, 2]) or (mes_user == 3 and dia_user <= 20):
            print("Usted está en Invierno")
        elif (mes_user == 3 and dia_user >= 21) or (mes_user in [4, 5]) or (mes_user == 6 and dia_user <= 20):
            print("Usted está en Primavera")
        elif (mes_user == 6 and dia_user >= 21) or (mes_user in [7, 8]) or (mes_user == 9 and dia_user <= 20):
            print("Usted está en Verano")
        elif (mes_user == 9 and dia_user >= 21) or (mes_user in [10, 11]) or (mes_user == 12 and dia_user <= 20):
            print("Usted está en Otoño")
    else:  # Hemisferio sur
        if (mes_user == 12 and dia_user >= 21) or (mes_user in [1, 2]) or (mes_user == 3 and dia_user <= 20):
            print("Usted está en Verano")
        elif (mes_user == 3 and dia_user >= 21) or (mes_user in [4, 5]) or (mes_user == 6 and dia_user <= 20):
            print("Usted está en Otoño")
        elif (mes_user == 6 and dia_user >= 21) or (mes_user in [7, 8]) or (mes_user == 9 and dia_user <= 20):
            print("Usted está en Invierno")
        elif (mes_user == 9 and dia_user >= 21) or (mes_user in [10, 11]) or (mes_user == 12 and dia_user <= 20):
            print("Usted está en Primavera")
