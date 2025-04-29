from tabulate import tabulate
import re

usuarios = []
continuar_menu = True
encontrado = True

while continuar_menu:
    try:    
        continuar = True
        print("\033[96m\n===============================================\nBienvenido al sistema de registro de estudiantes \n===============================================\033[0m")
        print("\033[93mPor favor seleccione una opción:\033[0m")
        print("\n1.) Agregar usuario")
        print("2.) Mostrar listado de usuarios")
        print("3.) Eliminar usuario")
        print("4.) Actualizar datos de usuario")

        opcion = int(input("\n\033[96mElije la opción que deseas: \033[0m"))
        
        if opcion == 1:
            while continuar:
                while True:
                    nombre = input("\nIngresa el nombre: ")
                    if nombre.replace(" ", "").isalpha():
                        break
                    else:
                        print("\033[91m\nEl nombre no puede contener numeros ni caracteres especiales.\033[0m")
                while True:        
                    apellido = input("\nIngresa el apellido: ")
                    if apellido.replace(" ", "").isalpha():
                        break
                    else:
                        print("\033[91m\nEl apellido no puede contener numeros ni caracteres especiales.\033[0m")
                while True:
                    correo = input("\nIngresa el correo con la estructura valida ejemplo(correo@dominio.com): ")
                    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
                    if not re.match(patron, correo):
                        print("\033[91m\nFormato de correo inválido. Debe tener formato (ejemplo@dominio.com)\033[0m")
                    else:
                        correo_duplicado = False
                        for usuario in usuarios:
                            if usuario[2].lower() == correo.lower():
                                correo_duplicado = True
                                break
                        if correo_duplicado:
                            print("\033[91m\nEste correo ya está registrado. Intenta con otro.\033[0m")
                        else:
                            break
                while True:
                    edad = input("\nIngresa la edad: ")
                    if edad.isdigit():
                        edad = int(edad)
                        break
                    else:
                        print("\033[91m\nLa edad no puede contener letras ni caracteres especiales\033[0m")   

                usuario = [nombre, apellido, correo, edad]
                usuarios.append(usuario)
                print("\033[92m\n¡Usuario agregado exitosamente!\033[0m")

                while continuar:
                    valor = input("\033[93m\n¿Deseas continuar ingresando usuario?: S()si N()no:\033[0m").lower()
                    if valor.lower() == "n":
                        continuar = False
                        while True:
                            salida = input("\033[93m\n¿Deseas volver al menu inicial?: S()si N()no:\033[0m").lower()
                            if salida.lower() == "s":
                                break
                            elif salida == "n":
                                continuar_menu = False
                                break 
                            else:
                                print("\033[91m\nPor favor ingresa 'N' para no o 'S' para sí.\033[0m")
                        break
                    elif valor == "s":
                        break
                    else:
                        print("\033[91m\nPor favor ingresa 'N' para no o 'S' para sí.\033[0m")
        elif opcion == 2:
            if len(usuarios) == 0:
                print("\033[91m\nNo hay usuarios registrados.\033[0m")
            else:
                tabla_mostrar = []
                for i, estudiante in enumerate(usuarios):
                    nombre, apellido, correo, edad = estudiante
                    tabla_mostrar.append([i+1, nombre, apellido, correo, f"{edad} años"])
                encabezado = ["#", "Nombre", "Apellido", "Correo", "Edad"]
                print(tabulate(tabla_mostrar, headers=encabezado, tablefmt="pretty"))
            while continuar:
                while True:
                    salida = input("\033[93m\n¿Deseas volver al menu inicial?: S()si N()no:\033[0m").lower()
                    if salida.lower() == "s":
                        break
                    elif salida == "n":
                        continuar_menu = False
                        break 
                    else:
                        print("\033[91m\nPor favor ingresa 'N' para no o 'S' para sí.\033[0m")
                break
        elif opcion == 3:
            if len(usuarios) == 0:
                print("\033[91m\nNo hay usuarios registrados.\033[0m")
                while True:
                    volver_menu = input("\033[93m\n¿Deseas volver al menú principal? S(si) / N(no): \033[0m").lower()
                    if volver_menu == "s":
                        break
                    elif volver_menu == "n":
                        continuar_menu = False
                        break
                    else:
                        print("\033[91m\nPor favor ingresa 'N' para no o 'S' para sí.\033[0m")
            else:
                while True:
                    tabla_eliminar = []
                    for i, estudiante in enumerate(usuarios):
                        nombre, apellido, correo, edad = estudiante
                        tabla_eliminar.append([i+1, nombre, apellido, correo, f"{edad} años"])
                    encabezado = ["#", "Nombre", "Apellido", "Correo", "Edad"]
                    print(tabulate(tabla_eliminar, headers=encabezado, tablefmt="pretty"))

                    entrada_e = input("\nIngrese el número del usuario que quiere eliminar: ")

                    if not entrada_e.isdigit():
                        print("\033[91m\nValor inválido. Digite un número válido.\033[0m")
                        continue

                    num_tabla2 = int(entrada_e) - 1
                    if 0 <= num_tabla2 < len(usuarios):
                        eliminado = usuarios.pop(num_tabla2)
                        print(f"\033[92m\nEl usuario {eliminado[0]} ha sido eliminado correctamente.\033[0m")
                        
                        continuar_eliminando = input("\033[93m\n¿Deseas eliminar otro usuario? S(si) / N(no): \033[0m").lower()
                        if continuar_eliminando == "n":
                            break
                    else:
                        print("\033[91m\nEl usuario no se encontró. Digite un registro existente.\033[0m")

                while True:
                    salir = input("\033[93m\n¿Deseas volver al menú principal? S(si) / N(no): \033[0m").lower()
                    if salir == "s":
                        break
                    elif salir == "n":
                        continuar_menu = False
                        break
                    else:
                        print("\033[91m\nPor favor ingresa 'N' para no o 'S' para sí.\033[0m")

        elif opcion == 4:
            if len(usuarios) == 0:
                print("\033[91m\nNo hay usuarios registrados.\033[0m")
                while True:
                    volver_menu = input("\033[93m\n¿Deseas volver al menú principal? S(si) / N(no): \033[0m").lower()
                    if volver_menu == "s":
                        break
                    elif volver_menu == "n":
                        continuar_menu = False
                        break
                    else:
                        print("\033[91m\nPor favor ingresa 'N' para no o 'S' para sí.\033[0m")
            else:
                while True:
                    tabla_actualizar = []
                    for i, estudiante in enumerate(usuarios):
                        nombre, apellido, correo, edad = estudiante
                        tabla_actualizar.append([i+1, nombre, apellido, correo, f"{edad} años"])
                    encabezado = ["#", "Nombre", "Apellido", "Correo", "Edad"]
                    print(tabulate(tabla_actualizar, headers=encabezado, tablefmt="pretty"))

                    entrada_a = input("\nIngrese el número del usuario que quiere actualizar: ")

                    if not entrada_a.isdigit():
                        print("\033[91m\nValor inválido. Digite un número válido.\033[0m")
                        continue

                    num_tabla = int(entrada_a) - 1
                    if 0 <= num_tabla < len(usuarios):
                        print(f"\nActualizando usuario: {usuarios[num_tabla][0]}")

                        nuevo_nombre = input("\nIngrese nuevo nombre (Enter para dejarlo igual): ")
                        if nuevo_nombre:
                            usuarios[num_tabla][0] = nuevo_nombre

                        nuevo_apellido = input("\nIngrese nuevo apellido (Enter para dejarlo igual): ")
                        if nuevo_apellido:
                            usuarios[num_tabla][1] = nuevo_apellido

                        while True:
                            nuevo_correo = input("\nIngrese nuevo correo (Enter para dejarlo igual): ")
                            if nuevo_correo == "":
                                break
                            patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
                            correos_existentes = [u[2] for idx, u in enumerate(usuarios) if idx != num_tabla]
                            if nuevo_correo in correos_existentes:
                                print("\033[91m\nEste correo ya está registrado. Ingresa uno diferente.\033[0m")
                            elif not re.match(patron, nuevo_correo):
                                print("\033[91m\nFormato de correo inválido.\033[0m")
                            else:
                                usuarios[num_tabla][2] = nuevo_correo
                                break

                        nueva_edad = input("\nIngrese nueva edad (Enter para dejarlo igual): ")
                        if nueva_edad:
                            if nueva_edad.isdigit():
                                usuarios[num_tabla][3] = int(nueva_edad)
                            else:
                                print("\033[91m\nEdad inválida. No se actualizó.\033[0m")

                        print("\033[92m\n¡Usuario actualizado exitosamente!\033[0m")

                        continuar_actualizando = input("\033[93m\n¿Deseas actualizar otro usuario? S(si) / N(no): \033[0m").lower()
                        if continuar_actualizando == "n":
                            break
                    else:
                        print("\033[91m\nNúmero de usuario no registrado por favor digita uno existente.\033[0m")
                while True:
                    salir = input("\033[93m\n¿Deseas volver al menú principal? S(si) / N(no): \033[0m").lower()
                    if salir == "s":
                        break
                    elif salir == "n":
                        continuar_menu = False
                        break
                    else:
                        print("\033[91m\nPor favor ingresa 'N' para no o 'S' para sí.\033[0m")
        else:
            print("\033[91m\nOpción no válida. Por favor, ingresa la correcta.\033[0m")
    except ValueError:
        print("\033[91m\nIngrese una opción válida.\033[0m")