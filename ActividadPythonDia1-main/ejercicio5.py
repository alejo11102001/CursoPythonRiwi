total_Cuenta = input("Digita el valor de la cuenta: ")
por_propina = input("Digita cuanta propina deseas dar(10, 15 o 20): ")

total_propina = (int(total_Cuenta) * int(por_propina))/100

print(f"El total de la propina es {total_propina}")