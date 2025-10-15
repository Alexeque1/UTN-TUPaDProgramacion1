# EJERCICIO 2
def agregar_prod (nombre, precio, cantidad, lista):
    lista.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})

def buscarProducto(nombre_prod, lista):
    encontrado = False
    for producto in lista:
        if producto["nombre"].lower() == nombre_prod.lower():
            print("Encontrado:")
            print(producto)
            encontrado = True
            break

    if not encontrado:
        print("Error, el producto no existe")


def validar_digito(tipo):
    while True:
        num = input(f"{tipo} > ")

        if not num.isdigit():
            print("Error, debe escribir un numero")
            continue
        break
    return int(num)


def programa_productos():
    productos = []
    with open('C:/Users/alexa/Documents/GitHub/UTN-TUPaDProgramacion1/8. Archivos CSV/productos.txt', 'r') as file:
        datos = file.readlines()
        print("-"*20)
        for linea in datos:
            partes = linea.strip().split(",")
            prod_nombre = partes[0]
            precio = int(partes[1])
            cantidad = int(partes[2])
            print(f"Producto: {prod_nombre} | Precio: {precio} | Cantidad: {cantidad}")
            print("-"*20)
            agregar_prod(prod_nombre, precio, cantidad, productos)


    print("Ingrese un nuevo producto: ")
    add_nombre = input("Nombre Producto > ")
    add_precio = validar_digito("Precio")
    add_cantidad = validar_digito("Cantidad")

    with open('C:/Users/alexa/Documents/GitHub/UTN-TUPaDProgramacion1/8. Archivos CSV/productos.txt', 'a') as file:
        nueva_linea = f"{add_nombre},{add_precio},{add_cantidad}\n"
        file.write(nueva_linea)
        agregar_prod(add_nombre, add_precio, add_cantidad, productos)

    print("Ingrese el nombre del producto que desea buscar")
    buscar_producto = input("> ")
    buscarProducto(buscar_producto, productos)

    with open('C:/Users/alexa/Documents/GitHub/UTN-TUPaDProgramacion1/8. Archivos CSV/productos.txt', 'w') as file:
        for producto in productos:
            linea_add = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
            file.write(linea_add)


programa_productos()