# Ejercicio 1
def factorial(n):
    return 1 if n == 0 else factorial(n - 1) * n


print("Elija un numero: ")
numero_user = int(input("> "))

for i in range(1, numero_user + 1):
    print(f"Factorial {i}: {factorial(i)}")


# Ejercicio 2
def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos - 1) + fibonacci(pos - 2)


num_user = int(input("Ingresa hasta qué posición de la serie Fibonacci quieres ver: "))

print("Serie de Fibonacci:")
for i in range(num_user + 1):
    print(fibonacci(i), end="  ")


# Ejercicio 3
def potencia(n, m):
    return 1 if m == 0 else n * potencia(n, m - 1)


print(potencia(3, 3))


# Ejercicio 4
def decimal_to_bin(dec):
    if dec < 2:
        return str(dec) 
    else:
        return decimal_to_bin(dec // 2) + str(dec % 2)


print(decimal_to_bin(12))


# Ejercicio 5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    
    if palabra[0].lower() != palabra[-1].lower():
        return False
    
    return es_palindromo(palabra[1:-1])


# Ejercicio 6
def suma_digitos(dig):
    if dig // 10 == 0:
        return dig
    else:
        return dig % 10 + suma_digitos(dig // 10)
    

# Ejercicio 7
def contar_bloques(n):
    if n <= 1:
        return 1
    else:
        return n + contar_bloques(n - 1)
    

# Ejercicio 8
def contar_digito(num, dig):
    if num < 10:
        return 1 if num == dig else 0
    elif num % 10 == dig:
        return 1 + contar_digito(num // 10, dig)
    return contar_digito(num // 10, dig)