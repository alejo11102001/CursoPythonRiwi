edad = int(input("Ingrese edad: "))

if edad <= 12:
    print("Eres un niño")
elif edad >= 12 and edad < 18:
    print("Eres adolentes")
elif edad >= 18 and edad < 60:
    print("Eres adulto")
else:
    print("Eres adulto mayor")