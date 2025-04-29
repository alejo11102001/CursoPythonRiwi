pares = []

for i in range(5):
    numero = int(input(f"Ingrese el numero {i+1}: "))
    if numero % 2 == 0:
        pares.append(numero)

print(pares)