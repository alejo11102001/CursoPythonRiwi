frutas = ["Mango", "Manzana", "Arroz"]
print(frutas)
eliminar = input("Ingrese fruta que desea eliminar: ")

if eliminar in frutas:
    frutas.remove(eliminar)
    print(frutas)