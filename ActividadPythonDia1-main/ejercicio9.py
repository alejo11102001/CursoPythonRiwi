año = input("Ingrese un año: ")
añoB = int(año)

if (añoB % 4 == 0 and añoB % 100 != 0):
    print("El año ingresado es bisiesto")
elif (añoB % 400 == 0):
    print("El año ingresado es bisiesto")
else:
    print("El año no es bisiesto")