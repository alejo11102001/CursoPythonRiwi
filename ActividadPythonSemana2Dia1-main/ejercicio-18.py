numeros = [10,20,30,40,50,60,70]

print(numeros)
numero = int(input("Numero a insertar: "))
posicion = int(input("En que posicion quiere insetarlo? (0-6): "))

numeros.insert(posicion, numero)
print(numeros)