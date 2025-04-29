numero = input("Ingrese el numero a adivinar: ")
num_secret = 7
cov_num = int(numero)

if (cov_num > num_secret):
    print("El numero que ingresaste es mayor al numero secreto")
elif(cov_num < num_secret):
    print("El numero que ingresaste es menor al numero secreto")
else:
    print("El numero que ingresaste es igual al numero secreto")
