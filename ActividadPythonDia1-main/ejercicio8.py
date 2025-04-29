peso = input("Ingrese su peso en Kg: ")
altura = input("Ingrese su altura en m: ")

IMC = float(peso)/(float(altura)**2)
print(IMC)

if (IMC < 18.5):
    print("Tienes bajo peso")
elif (18.5 <= IMC < 24.5):
    print("Tienes peso normal")
elif (25 <= IMC < 29.9):
    print("Tienes sobrepeso")
else:
    print("Tienes obecidad")