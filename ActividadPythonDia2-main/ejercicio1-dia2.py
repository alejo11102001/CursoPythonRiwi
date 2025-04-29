num1 = int(input("Digite numero 1: "))
num2 = int(input("Digite numero 2: "))
num3 = int(input("Digite numero 3: "))

if (num1 < num2 and num1 < num3):
    print(f"El numero mas pequeño es el numero 1: {num1}")
elif (num2 < num1 and num2 < num3):
    print(f"El numero mas pequeño es el numero 2: {num2}")
else:
    print(f"El numero mas pequeño es el numero 3: {num3}")