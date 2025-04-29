from tabulate import tabulate
import re

contactos_diccionario = {}
continuar_menu = True
contacto = 0

while continuar_menu:
    try:
        continuar = True
        print("\n\033[96m===============================================\nBienvenido al sistema de agenda de contactos\n===============================================\033[0m")
        print("\033[93mPor favor seleccione una opción:\033[0m")
        print("\n1.) Agregar contacto")
        print("2.) Mostrar listado de contactos")
        print("3.) Actualizar datos de un contacto")
        print("4.) Eliminar contacto")

        opcion = int(input("\nElije la opción que deseas: "))

        if opcion not in (1, 2, 3, 4):
            print("\033[91m\nOpción inválida. Por favor elige una opción entre 1 y 4.\033[0m")
            continue

        if opcion == 1:
            while continuar:
                while True:
                    nombre = input("\nIngresa el nombre del contacto: ")
                    if nombre.replace(" ", "").isalpha():
                        break
                    else:
                        print("\033[91m\nEl nombre no puede contener números ni caracteres especiales.\033[0m")
                while True:
                    telefono = input("\nIngresa el número del contacto: ")
                    if telefono.isdigit():
                        telefono = int(telefono)
                        break
                    else:
                        print("\033[91m\nEl número no puede contener caracteres especiales ni letras.\033[0m")
                while True:
                    email = input("\nIngresa el correo con formato válido (ejemplo@dominio.com): ")
                    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
                    if not re.match(patron, email):
                        print("\033[91m\nFormato de correo inválido.\033[0m")
                    else:
                        correo_duplicado = False
                        for datos in contactos_diccionario.values():
                            if datos["email"].lower() == email.lower():
                                correo_duplicado = True
                                break
                        if correo_duplicado:
                            print("\033[91m\nEste correo ya está registrado. Intenta con otro.\033[0m")
                        else:
                            break

                contacto += 1
                contactos_diccionario[contacto] = {
                    "nombre": nombre,
                    "telefono": telefono,
                    "email": email
                }
                print("\033[92m\nContacto agregado correctamente.\033[0m")

                while True:
                    valor = input("\033[93m\n¿Deseas continuar ingresando contactos? (S/N):\033[0m ").lower()
                    if valor == "n":
                        continuar = False
                        while True:
                            salida = input("\033[93m\n¿Deseas volver al menú inicial? (S/N):\033[0m ").lower()
                            if salida in ("s", "n"):
                                if salida == "n":
                                    continuar_menu = False
                                break
                            else:
                                print("\033[91m\nPor favor ingresa 'S' para sí o 'N' para no.\033[0m")
                        break
                    elif valor == "s":
                        break
                    else:
                        print("\033[91m\nPor favor ingresa 'S' para sí o 'N' para no.\033[0m")

        elif opcion == 2:
            if not contactos_diccionario:
                print("\033[91m\nNo hay contactos registrados.\033[0m")
                while True:
                    salida = input("\033[93m\n¿Deseas volver al menú inicial? (S/N):\033[0m ").lower()
                    if salida in ("s", "n"):
                        if salida == "n":
                            continuar_menu = False
                        break
                    else:
                        print("\033[91m\nPor favor ingresa 'S' para sí o 'N' para no.\033[0m")
            else:
                tabla = [[key, datos["nombre"], datos["telefono"], datos["email"]] for key, datos in contactos_diccionario.items()]
                print(tabulate(tabla, headers=["#Contacto", "Nombre", "Telefono", "Correo"], tablefmt="pretty"))

                while True:
                    buscar = input("\033[93m\n¿Deseas buscar un contacto específico? (S/N):\033[0m ").lower()
                    if buscar == "n":
                        while True:
                            salida = input("\033[93m\n¿Deseas volver al menú inicial? (S/N):\033[0m ").lower()
                            if salida in ("s", "n"):
                                if salida == "n":
                                    continuar_menu = False
                                break
                            else:
                                print("\033[91m\nPor favor ingresa 'S' para sí o 'N' para no.\033[0m")
                        break
                    elif buscar == "s":
                        nombre_buscar = input("\nIngresa el nombre del contacto: ").lower()
                        encontrado = False
                        for key, datos in contactos_diccionario.items():
                            if nombre_buscar in datos["nombre"].lower():
                                tabla = [[key, datos["nombre"], datos["telefono"], datos["email"]]]
                                print(tabulate(tabla, headers=["#Contacto", "Nombre", "Telefono", "Correo"], tablefmt="pretty"))
                                encontrado = True
                                break
                        if not encontrado:
                            print("\033[91m\nNo se encontró ningún contacto con ese nombre.\033[0m")
                    else:
                        print("\033[91m\nPor favor ingresa 'S' para sí o 'N' para no.\033[0m")

        elif opcion == 3:
            if not contactos_diccionario:
                print("\033[91m\nNo hay contactos registrados.\033[0m")
            else:
                while True:
                    tabla = [[key, datos["nombre"], datos["telefono"], datos["email"]] for key, datos in contactos_diccionario.items()]
                    print(tabulate(tabla, headers=["#Contacto", "Nombre", "Telefono", "Correo"], tablefmt="pretty"))

                    try:
                        id_actualizar = int(input("\nIngresa el ID del contacto que quieres actualizar: "))
                        if id_actualizar not in contactos_diccionario:
                            print("\033[91m\nID inválido. Por favor intenta de nuevo.\033[0m")
                            continue
                    except ValueError:
                        print("\033[91m\nID inválido. Debes ingresar un número.\033[0m")
                        continue

                    datos_actualizar = contactos_diccionario[id_actualizar]
                    print(f"\n\033[96mActualizando contacto: {datos_actualizar['nombre']}\033[0m")

                    while True:
                        confirmar = input("\n\033[93m¿Estás seguro que deseas actualizar este contacto? (S/N): \033[0m").lower()
                        if confirmar == "s":
                            nuevo_nombre = input("\nNuevo nombre (Enter para mantener actual): ")
                            nuevo_telefono = input("\nNuevo teléfono (Enter para mantener actual): ")
                            nuevo_email = input("\nNuevo correo (Enter para mantener actual): ")

                            if nuevo_nombre:
                                if nuevo_nombre.replace(" ", "").isalpha():
                                    datos_actualizar["nombre"] = nuevo_nombre
                                else:
                                    print("\033[91m\nNombre inválido. No se actualizó.\033[0m")
                            if nuevo_telefono:
                                if nuevo_telefono.isdigit():
                                    datos_actualizar["telefono"] = int(nuevo_telefono)
                                else:
                                    print("\033[91m\nTeléfono inválido. No se actualizó.\033[0m")
                            if nuevo_email:
                                patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
                                if re.match(patron, nuevo_email):
                                    datos_actualizar["email"] = nuevo_email
                                else:
                                    print("\033[91m\nCorreo inválido. No se actualizó.\033[0m")

                            print("\033[92m\nContacto actualizado correctamente.\033[0m")
                            break
                        elif confirmar == "n":
                            print("\033[93m\nActualización cancelada.\033[0m")
                            break
                        else:
                            print("\033[91m\nPor favor ingresa 'S' para sí o 'N' para no.\033[0m")

                    repetir = input("\033[93m\n¿Deseas actualizar otro contacto? (S/N): \033[0m").lower()
                    if repetir != "s":
                        while True:
                            salida = input("\033[93m\n¿Deseas volver al menú principal? (S/N): \033[0m").lower()
                            if salida in ("s", "n"):
                                if salida == "n":
                                    continuar_menu = False
                                break
                            else:
                                print("\033[91m\nPor favor ingresa 'S' para sí o 'N' para no.\033[0m")
                        break

        elif opcion == 4:
            if not contactos_diccionario:
                print("\033[91m\nNo hay contactos registrados.\033[0m")
            else:
                while True:
                    if not contactos_diccionario:
                        print("\033[91m\nYa no hay contactos para eliminar.\033[0m")
                        while True:
                            salida = input("\033[93m\n¿Deseas volver al menú principal? (S/N):\033[0m ").lower()
                            if salida in ("s", "n"):
                                if salida == "n":
                                    continuar_menu = False
                                break
                            else:
                                print("\033[91m\nPor favor ingresa 'S' para sí o 'N' para no.\033[0m")
                        break

                    tabla = [[key, datos["nombre"], datos["telefono"], datos["email"]] for key, datos in contactos_diccionario.items()]
                    print(tabulate(tabla, headers=["#Contacto", "Nombre", "Telefono", "Correo"], tablefmt="pretty"))

                    try:
                        id_eliminar = int(input("\nIngrese el ID del contacto que desea eliminar: "))
                        if id_eliminar not in contactos_diccionario:
                            print("\033[91m\nID inválido. Inténtalo de nuevo.\033[0m")
                            continue
                    except ValueError:
                        print("\033[91m\nDebes ingresar un número válido.\033[0m")
                        continue

                    datos_eliminar = contactos_diccionario[id_eliminar]
                    
                    while True:
                        confirmar = input(f"\033[93m\n¿Estás seguro que deseas eliminar a '{datos_eliminar['nombre']}'? (S/N): \033[0m").lower()
                        if confirmar == "s":
                            del contactos_diccionario[id_eliminar]
                            print("\033[92m\nContacto eliminado correctamente.\033[0m")
                            break
                        elif confirmar == "n":
                            print("\033[93m\nEliminación cancelada.\033[0m")
                            break
                        else:
                            print("\033[91m\nPor favor ingresa 'S' para sí o 'N' para no.\033[0m")

                    if contactos_diccionario: 
                        repetir = input("\033[93m\n¿Deseas eliminar otro contacto? (S/N): \033[0m").lower()
                        if repetir != "s":
                            while True:
                                salida = input("\033[93m\n¿Deseas volver al menú principal? (S/N): \033[0m").lower()
                                if salida in ("s", "n"):
                                    if salida == "n":
                                        continuar_menu = False
                                    break
                                else:
                                    print("\033[91m\nPor favor ingresa 'S' para sí o 'N' para no.\033[0m")
                            break
    except ValueError:
        print("\033[91m\nPor favor ingresa una opción válida.\033[0m")
