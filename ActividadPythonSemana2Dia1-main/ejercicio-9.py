ingresa_nota = float(input("Ingresa una nota(0-10): "))

if ingresa_nota > 5:
    print("suspendio")
elif ingresa_nota >= 5 and ingresa_nota < 7:
    print("Aprobado")
elif ingresa_nota >= 7 and ingresa_nota <= 10:
    print("SObresaliente")
else:
    print("No existe esa nota")