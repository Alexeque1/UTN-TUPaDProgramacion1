# Ejercicio 1
print("-"*40)
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300
print(f"Precios de las frutas: {precios_frutas}")
print("-"*40)

# Ejercicio 2
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800
print(f"Precio actualizado de las frutas despues de los cambios:")
print(f"{precios_frutas}")
print("-"*40)

# Ejercicio 3
print(f"Lista de las frutas sin los precios: ")
print(f"{precios_frutas.keys()}")
print("-"*40)

# Ejercicio 4
contactos_telf = {}


def agregar_contactos():
    print("Por favor, agregue los contactos:")
    for i in range(5):
        while True:
            print("-"*20)
            print(f"Nombre de Contacto {i + 1}:")
            nombre_telf = input("> ")
            print("Numero de Contacto:")
            numero_telf = input("> ")
        
            if nombre_telf in contactos_telf:
                print("Error, el contacto ya existe")
                continue
            else:
                nombre_telf = nombre_telf.lower()
                contactos_telf[nombre_telf] = numero_telf
                break


agregar_contactos()

print("Busque a un usuario en la agenda: ")
buscar = input("> ").lower()

if buscar in contactos_telf:
    print("-"*20)
    print("El contacto existe: ")
    print(f"Nombre: {buscar}")
    print(f"Numero de Telefono: {contactos_telf[buscar]}")
else:
    print("El contacto no existe")
print("-"*40)

# Ejercicio 5
print("Ingrese una frase: ")
frase = input("> ").split(" ")
cuantas_veces = {}

for palabra in frase:
    if palabra not in cuantas_veces:
        cuantas_veces[palabra] = 0
    cuantas_veces[palabra] += 1

print(f"Palabras unicas: {set(frase)}")
print(f"Cuantas veces aparece cada palabra: {cuantas_veces}")
print("-"*40)

# Ejercicio 6
notas = {}
for i in range(3):
    notas_alumno = []
    print(f"Ingrese el nombre del alumno {i + 1}:")
    nombre_alumno = input("> ")
    for i in range(3):
        print(f"Ingrese la nota {i + 1}:")
        nota = int(input("> "))
        notas_alumno.append(nota)
    notas[nombre_alumno] = tuple(notas_alumno)

for i, (alumno, notas) in enumerate(notas.items(), start=1):
    print("-"*20)
    print(f"Notas de Alumno {i}:")
    print(f"{alumno}")
    print(f"Notas: {notas}")
    print(f"Promedio: {round(sum(notas) / len(notas), 2)}")
print("-"*40)

# Ejercicio 7
parcial1 = {"Alex", "Martina", "Fernanda", "Alejandro", "Nina", "Hugo", "Bruno", "Maria", "Jose"}
parcial2 = {"Alex", "Vanina", "Nina", "Sandra", "Ricardo", "Hugo", "Bruno", "Carlos", "Gonza", "Karina", "Maria"}

print(f"Los que aprobaron ambos examenes: {parcial1 & parcial2}")
print(f"Aprobaron solo uno de los dos: {parcial1 ^ parcial2}")
print(f"Total de alumnos que aprobaron al menos un examen: {parcial1 | parcial2}")
print("-"*40)

# Ejercicio 8
stock_productos = {
    "arroz": 25,
    "fideos": 40,
    "aceite": 15,
    "azúcar": 30,
    "harina": 20,
    "leche": 50,
    "pan": 35,
    "huevos": 60
}

while True:
    print("Ingrese la opcion: ")
    print("(1) Consultar stock")
    print("(2) Agregar unidades al stock")
    print("(3) Agregar un nuevo producto")
    print("(0) Salir")
    opcion = input("> ")

    if opcion not in ("1", "2", "3", "0"):
        print("Error, debe escojer una opcion valida")
    
    print("-"*20)
    match opcion:
        case "1":
            print("¿Que producto quiere consultar stock?")
            producto_stock = input("> ")
            print("-"*20)

            if producto_stock.lower() not in stock_productos:
                print("El producto no existe en stock")
            else:
                print(f"El producto {producto_stock} cuenta con {stock_productos[producto_stock.lower()]} en stock")
        
        case "2":
            print("¿A que producto desea agregar stock?")
            producto_add_stock = input("> ")
            print("-"*20)

            if producto_add_stock.lower() not in stock_productos:
                print("El producto no existe en stock")
            else:
                print("¿Cuantas unidades?")
                unidades_add = int(input("> "))

                stock_productos[producto_add_stock.lower()] += unidades_add

                print(f"Se ha agregado {unidades_add} a {producto_add_stock}, ahora tiene {stock_productos[producto_add_stock.lower()]}")
        
        case "3":
            print("¿Que producto desea agregar?")
            producto_add = input("> ")

            if producto_add.lower() in stock_productos:
                print("El producto ya existe en stock")
            else:
                stock_productos[producto_add.lower()] = 0

                print(f"Se ha agregado el producto {producto_add} a stock")

        case "0":
            print("Usted salio del programa")
            break
        
    print("¿Desea hacerlo otra vez?")
    print("(1) Si (2) No")
    otra_vez = input("> ")

    if otra_vez in ("Si", "1"):
        continue
    else:
        break

print("-"*40)

# Ejercicio 9
agenda = {
    ("Lunes", "09:00"): "Reunión de equipo",
    ("Lunes", "14:00"): "Clase de inglés",
    ("Martes", "10:30"): "Consulta médica",
    ("Miércoles", "16:00"): "Gimnasio",
    ("Jueves", "11:00"): "Llamada con cliente",
    ("Viernes", "18:00"): "Cena con amigos",
    ("Sábado", "15:00"): "Partido de fútbol",
    ("Domingo", "12:00"): "Almuerzo familiar"
}

dia_user = input("Ingresá el día: ")
hora_user = input("Ingresá la hora (por ejemplo 14:00): ")
evento = False

if (dia_user, hora_user) in agenda:
        evento = agenda[(dia_user, hora_user)]

if evento:
    print(f"El {dia_user} a las {hora_user} tenés: {evento}")
else:
    print(f"No hay actividades registradas el {dia_user} a las {hora_user}.")

print("-"*40)

# Ejercicio 10
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "México": "Ciudad de México",
    "España": "Madrid",
    "Francia": "París",
    "Italia": "Roma",
    "Japón": "Tokio",
    "Canadá": "Ottawa",
    "Australia": "Canberra"
}

ciudades_paises = {}

for pais, capital in paises_capitales.items():
    ciudades_paises[capital] = pais

print(ciudades_paises)
print("-"*40)