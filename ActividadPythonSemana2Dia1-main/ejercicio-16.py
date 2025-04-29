numeros = [3,6,8,7,2,4]

buscar = int(input("Ingrese el numero que quiere buscar: "))

if buscar in numeros:
    posicion = numeros.index(buscar)
    print(buscar, posicion) 
