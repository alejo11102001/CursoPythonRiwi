licencia = input("Lleva licencia?: ")
casco = input("Lleva casco: ")

if licencia != "si" or casco != "si":
    print("No puede conducir")
else:
    print("Puede conducir")