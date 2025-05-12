# CursoPythonRiwi

## Ejercicios Semanales de Python

Este repositorio contiene ejercicios semanales de Python que hemos realizado a lo largo del curso. Los ejercicios están organizados en carpetas según la semana correspondiente.

### Actividad 1 - Semana 1 - Dia 1

En esta carpeta encontrara los 10 ejercicios de python que hicimos el primer dia de la semana 1.

### Actividad 2 - Semana 1 - Dia 2

En esta carpeta encontrara los 5 ejercicios de python que hicimos el segundo dia de la semana 1.

### Actividad 3 - Semana 1 - Dia 3

En esta carpeta encontrara el ejercicio CRUD de python que hicimos el tercer dia de la semana 1 sobre ingresar estudiantes a una lista.

### Activida 4 - Semana 1 - Dia 4

En esta carpeta encontrara los ejercicios CRUD de python que hicimos el cuarto dia de la semana 1 sobre ingresar libros y contactos a una diccionario.

### Actividad 1 -Semana 2 - Dia 1

En esta carpeta encontrara los ejercicios de repaso de python que hicimos el primer dia de la semana 2.

### Actividad 2 -Semana 2 - Dia 2

En esta carpeta encontrara la actividad de Sistema de Gestión y Costeo de Equipaje Aéreo ubicado en la pagina learn.

### Actividad 3 -Semana 2 - Dia 3

En esta carpeta encontrara la información de un archivo.txt organizada en una tabla con colores distintivos.

### Actividad 1 -Semana 3 - Dia 1

En esta carpeta encontrara la actividad del simulacro de un cajero personal.

### Actividad 2 -Semana 3 - Dia 2

En esta carpeta encontrara los ejercicios de funciones que van desde el nivel basico, pasa por intermedio y termina en avanzado.

### Actividad 3 -Semana 3 - Dia 3

En esta carpeta encontrara el ejercicio del diccionario de estudiantes con funciones.

# Diccionario para almacenar los productos del inventario
inventario = {}

# Función para agregar un producto al inventario
def agregar_producto(nombre, precio, cantidad):
    inventario[nombre.lower()] = {"precio": precio, "cantidad": cantidad}
    print(f"Producto '{nombre}' agregado correctamente.\n")

# Función para consultar un producto en el inventario
def consultar_producto(nombre):
    producto = inventario.get(nombre.lower())
    if producto:
        print(f"\nProducto: {nombre}")
        print(f"Precio: ${producto['precio']:.2f}")
        print(f"Cantidad: {producto['cantidad']}\n")
    else:
        print(f"\nEl producto '{nombre}' no se encuentra en el inventario.\n")

# Función para actualizar el precio de un producto
def actualizar_precio(nombre, nuevo_precio):
    if nuevo_precio <= 0:
        print("\nError: El precio debe ser un número positivo.\n")
        return
    producto = inventario.get(nombre.lower())
    if producto:
        producto['precio'] = nuevo_precio
        print(f"\nPrecio del producto '{nombre}' actualizado correctamente.\n")
    else:
        print(f"\nEl producto '{nombre}' no se encuentra en el inventario.\n")

# Función para eliminar un producto del inventario
def eliminar_producto(nombre):
    if nombre.lower() in inventario:
        del inventario[nombre.lower()]
        print(f"\nProducto '{nombre}' eliminado correctamente.\n")
    else:
        print(f"\nEl producto '{nombre}' no existe en el inventario.\n")

# Función para calcular el valor total del inventario
def calcular_valor_total():
    total = sum(info["precio"] * info["cantidad"] for info in inventario.values())
    print(f"\nValor total del inventario: ${total:.2f}\n")

# Función para agregar productos iniciales
def agregar_productos_iniciales():
    agregar_producto("Manzanas", 0.50, 100)
    agregar_producto("Bananas", 0.30, 150)
    agregar_producto("Naranjas", 0.60, 80)
    agregar_producto("Leche", 1.20, 50)
    agregar_producto("Pan", 1.00, 60)

# Función para mostrar el menú interactivo
def mostrar_menu():
    print("=== MENÚ DE INVENTARIO ===")
    print("1. Agregar producto")
    print("2. Consultar producto")
    print("3. Actualizar precio de producto")
    print("4. Eliminar producto")
    print("5. Calcular valor total del inventario")
    print("6. Mostrar todos los productos")
    print("0. Salir")

# Programa principal
if __name__ == "__main__":
    agregar_productos_iniciales()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            try:
                precio = float(input("Precio del producto: "))
                cantidad = int(input("Cantidad disponible: "))
                agregar_producto(nombre, precio, cantidad)
            except ValueError:
                print("Error: Ingrese un número válido para el precio o cantidad.\n")
        elif opcion == "2":
            nombre = input("Nombre del producto a consultar: ")
            consultar_producto(nombre)
        elif opcion == "3":
            nombre = input("Nombre del producto: ")
            try:
                nuevo_precio = float(input("Nuevo precio: "))
                actualizar_precio(nombre, nuevo_precio)
            except ValueError:
                print("Error: Ingrese un precio válido.\n")
        elif opcion == "4":
            nombre = input("Nombre del producto a eliminar: ")
            eliminar_producto(nombre)
        elif opcion == "5":
            calcular_valor_total()
        elif opcion == "6":
            if inventario:
                print("\n=== LISTA DE PRODUCTOS ===")
                for nombre, datos in inventario.items():
                    print(f"- {nombre.title()} | Precio: ${datos['precio']:.2f} | Cantidad: {datos['cantidad']}")
                print()
            else:
                print("El inventario está vacío.\n")
        elif opcion == "0":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.\n")
