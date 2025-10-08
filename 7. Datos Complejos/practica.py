# Ejercicio 9
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