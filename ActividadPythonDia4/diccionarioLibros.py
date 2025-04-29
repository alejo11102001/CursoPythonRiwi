from tabulate import tabulate
libro_diccionario = {}
continuar_menu = True
isbn = 0

while continuar_menu:
    try:    
        continuar = True
        print("\033[96m\n===============================================\nBienvenido al sistema de registro de libros \n===============================================\033[0m")
        print("\033[93mPor favor seleccione una opción:\033[0m")
        print("\n1.) Agregar libro")
        print("2.) Mostrar listado de libros")
        print("3.) Eliminar libro")
        print("4.) Actualizar datos de un libro")

        opcion = int(input("\n\033[93mElije la opción que deseas: \033[0m"))

        if opcion not in (1, 2, 3, 4):
            print("\033[91m\nOpción inválida. Por favor elige una opción entre 1 y 4.\033[0m")
            continue
        
        if opcion == 1:
            while continuar:
                while True:
                    titulo = input("\nIngresa el titulo del libro: ")
                    if titulo.replace(" ", "").isalpha():
                        break
                    else:
                        print("\n\033[91mEl titulo no puede contener numeros ni caracteres especiales.\033[0m")
                while True:        
                    autor = input("\nIngresa el autor del libro: ")
                    if autor.replace(" ", "").isalpha():
                        break
                    else:
                        print("\n\033[91mEl autor no puede contener numeros ni caracteres especiales.\033[0m")
                while True:
                    año_publicacion = input("\nIngresa el año de publicación: ")
                    if año_publicacion.isdigit():
                        año_publicacion = int(año_publicacion)
                        break
                    else:
                        print("\n\033[91mLa edad no puede contener letras ni caracteres especiales.\033[0m")   

                isbn = isbn + 1
                libro_diccionario[isbn] = {
                    "titulo": titulo,
                    "autor": autor,
                    "año": año_publicacion
                }
                print("\n\033[91mLibro agregado correctamente.\033[0m")
                while continuar:
                    valor = input("\033[93m\n¿Deseas continuar ingresando libros?: S()si N()no:\033[0m").lower()
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
            if len(libro_diccionario) == 0:
                print("\033[91m\nNo hay libros registrados\033[0m")
                while True:
                    salida = input("\033[93m\n¿Deseas volver al menú inicial?: S()si N()no:\033[0m").lower()
                    if salida == "s":
                        break
                    elif salida == "n":
                        continuar_menu = False
                        break
                    else:
                        print("\033[91m\nPor favor ingresa 'S' para sí o 'N' para no.\033[0m")
            else:
                tabla_mostrar = []
                for i, (isbn, datos) in enumerate(libro_diccionario.items()):
                    titulo = datos["titulo"]
                    autor = datos["autor"]
                    año_publicacion = datos["año"]
                    tabla_mostrar.append([isbn, titulo, autor, año_publicacion])
                    
                encabezado = ["#ISBN", "Titulo", "Autor", "Año de publicación"]
                print(tabulate(tabla_mostrar, headers=encabezado, tablefmt="pretty"))

                while True: 
                    desea_buscar = input("\033[93m\n¿Deseas buscar un libro en específico?: S()si N()no: \033[0m").lower()
                    if desea_buscar == "s":
                        while True:
                            busqueda_tipo = input("\033[93m\n¿Quieres buscar por ID (I) o por título (T)?: \033[0m").lower()
                            if busqueda_tipo == "i":
                                while True:
                                    try:
                                        num_bus = int(input("\nIngrese el ID del libro que quiere buscar: "))
                                        if num_bus in libro_diccionario:
                                            tabla_ver = []
                                            datos = libro_diccionario[num_bus]
                                            titulo = datos["titulo"]
                                            autor = datos["autor"]
                                            año_publicacion = datos["año"]
                                            tabla_ver.append([num_bus, titulo, autor, año_publicacion])
                                            print(tabulate(tabla_ver, headers=["#ISBN", "Titulo", "Autor", "Año de publicación"], tablefmt="pretty"))
                                            break
                                        else:
                                            print("\033[91m\nEl ID ingresado no está registrado. Intenta de nuevo.\033[0m")
                                    except ValueError:
                                        print("\033[91m\nPor favor ingresa un número válido para el ID.\033[0m")
                                break 
                            elif busqueda_tipo == "t":
                                while True:
                                    titulo_bus = input("\nIngrese el título del libro que quiere buscar: ").strip().lower()
                                    if titulo_bus == "":
                                        print("\033[91m\nEl título no puede estar vacío. Por favor ingrésalo nuevamente.\033[0m")
                                        continue
                                    encontrado = False
                                    for isbn, datos in libro_diccionario.items():
                                        if titulo_bus in datos["titulo"].lower():
                                            datos_libro = libro_diccionario[isbn]
                                            tabla_ver = [[isbn, datos_libro["titulo"], datos_libro["autor"], datos_libro["año"]]]
                                            print(tabulate(tabla_ver, headers=["#ISBN", "Titulo", "Autor", "Año de publicación"], tablefmt="pretty"))
                                            encontrado = True
                                            break
                                    if not encontrado:
                                        print("\033[91m\nNo se encontró ningún libro con ese título. Intenta nuevamente.\033[0m")
                                    else:
                                        break 
                                break
                            else:
                                print("\033[91m\nPor favor ingresa 'I' para ID o 'T' para Título.\033[0m")
                    elif desea_buscar == "n":
                        while True:
                            salida = input("\033[93m\n¿Deseas volver al menú inicial?: S()si N()no:\033[0m").lower()
                            if salida == "s":
                                break
                            elif salida == "n":
                                continuar_menu = False
                                break
                            else:
                                print("\033[91m\nPor favor ingresa 'S' para sí o 'N' para no.\033[0m")
                        break
                    else:
                        print("\033[91m\nPor favor ingresa 'S' para sí o 'N' para no.\033[0m")
        elif opcion == 3:
            if len(libro_diccionario) == 0:
                print("\033[91m\nNo hay libros registrados\033[0m")
                while True:
                    salida = input("\033[93m\n¿Deseas volver al menú inicial?: S()si N()no:\033[0m").lower()
                    if salida == "s":
                        break
                    elif salida == "n":
                        continuar_menu = False
                        break
                    else:
                        print("\033[91m\nPor favor ingresa 'S' para sí o 'N' para no.\033[0m")
            else:
                while True:
                    tabla_eliminar = []
                    for i, (isbn, datos) in enumerate(libro_diccionario.items()):
                        titulo = datos["titulo"]
                        autor = datos["autor"]
                        año_publicacion = datos["año"]
                        tabla_eliminar.append([isbn, titulo, autor, año_publicacion])
                        
                    encabezado = ["#ISBN", "Titulo", "Autor", "Año de publicacion"]
                    print(tabulate(tabla_eliminar, headers=encabezado, tablefmt="pretty"))

                    try:
                        num_tabla2 = int(input("\nIngrese el ID del libro que quiere eliminar: "))
                        if num_tabla2 in libro_diccionario:
                            eliminado = libro_diccionario.pop(num_tabla2)
                            print(f"\033[92m\nEl libro {eliminado['titulo']} ha sido eliminado correctamente\033[0m")
                    
                            if len(libro_diccionario) == 0:
                                print("\033[92m\nYa no hay más libros registrados.\033[0m")
                                break

                            while True:
                                    continuar_eliminado = input("\033[93m\n¿Deseas eliminar otro libro? S(si) N(no): \033[0m").lower()
                                    if continuar_eliminado == "s":
                                        break
                                    elif continuar_eliminado == "n":
                                        break
                                    else:
                                        print("\033[91m\nPor favor ingresa 'S' para sí o 'N' para no.\033[0m")
                            if continuar_eliminado == "n":
                                break
                        else:
                            print("\033[91m\nEl libro no se encontro en la base de datos digite un registro existente\033[0m") 
                    except ValueError:
                        print("\033[91m\nEntrada inválida. Debes ingresar un número válido.\033[0m")   
                while True:
                    salida = input("\033[93m\n¿Deseas volver al menu inicial?: S()si N()no:\033[0m").lower()
                    if salida.lower() == "s":
                        break
                    elif salida == "n":
                        continuar_menu = False
                        break 
                    else:
                        print("\033[91m\nPor favor ingresa 'N' para no o 'S' para sí.\033[0m")
        elif opcion == 4:
            if len(libro_diccionario) == 0:
                print("\033[91m\nNo hay libros registrados.\033[0m")
                while True:
                    salida = input("\033[93m\n¿Deseas volver al menú inicial?: S(si) N(no): \033[0m").lower()
                    if salida == "s":
                        break
                    elif salida == "n":
                        continuar_menu = False
                        break
                    else:
                        print("\033[91m\nPor favor ingresa 'S' para sí o 'N' para no.\033[0m")
            else:
                while True:
                    tabla_actualizar = []
                    for i, (isbn, datos) in enumerate(libro_diccionario.items()):
                        titulo = datos["titulo"]
                        autor = datos["autor"]
                        año_publicacion = datos["año"]
                        tabla_actualizar.append([isbn, titulo, autor, año_publicacion])

                    encabezado = ["#ISBN", "Titulo", "Autor", "Año de publicación"]
                    print(tabulate(tabla_actualizar, headers=encabezado, tablefmt="pretty"))

                    try:
                        num_isbn = int(input("\nIngrese el ID del libro que quiere actualizar: "))
                        if num_isbn in libro_diccionario:
                            print(f"\nActualizando libro: {libro_diccionario[num_isbn]['titulo']}")

                            nuevo_titulo = input("\nIngrese nuevo título del libro (Enter para dejar igual): ")
                            nuevo_autor = input("\nIngrese nuevo autor (Enter para dejar igual): ")
                            nuevo_año = input("\nIngrese nuevo año de publicación (Enter para dejar igual): ")

                            if nuevo_titulo:
                                libro_diccionario[num_isbn]["titulo"] = nuevo_titulo
                            if nuevo_autor:
                                libro_diccionario[num_isbn]["autor"] = nuevo_autor
                            if nuevo_año:
                                if nuevo_año.isdigit():
                                    libro_diccionario[num_isbn]["año"] = int(nuevo_año)
                                else:
                                    print("\033[91m\nEl año debe ser un número válido. No se actualizó el año.\033[0m")

                            print("\033[92m\nLibro actualizado correctamente.\033[0m")
                        else:
                            print("\033[91m\nEl ID ingresado no existe en la base de datos.\033[0m")
                    except ValueError:
                        print("\033[91m\nEntrada inválida. Debes ingresar un número válido.\033[0m")

                    while True:
                        salida = input("\033[93m\n¿Deseas actualizar otro libro? S(si) N(no): \033[0m").lower()
                        if salida == "s":
                            break 
                        elif salida == "n":
                            break 
                        else:
                            print("\033[91m\nPor favor ingresa 'S' para sí o 'N' para no.\033[0m")

                    if salida == "n":
                        break

                while True:
                    volver_menu = input("\033[93m\n¿Deseas volver al menú inicial?: S(si) N(no): \033[0m").lower()
                    if volver_menu == "s":
                        break
                    elif volver_menu == "n":
                        continuar_menu = False
                        break
                    else:
                        print("\033[91m\nPor favor ingresa 'S' para sí o 'N' para no.\033[0m")
    except ValueError:
        print("\033[91m\nIngrese una opción valida\033[0m")