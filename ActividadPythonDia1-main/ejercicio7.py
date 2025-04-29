numero1 = input("Ingrese numero 1: ")
numero2 = input("Ingrese numero 2: ")

cov_num1 = int(numero1)
cov_num2 = int(numero2)

if (cov_num1 > cov_num2):
    print("El numero 1 es mayor al numero 2")
elif(cov_num1 < cov_num2):
    print("El numero 2 es mayor al numero 1")
else:
    print("Los numeros son iguales")
