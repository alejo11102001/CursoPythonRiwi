from tabulate import tabulate  # Used to display data in a tabular format

# Dictionary that stores student data, using their ID as the key
students = {
    1000640800: {"Name": "Carlos Pérez", "Age": 20, "ID": 1000640800, "Note": 4.2},
    1000640801: {"Name": "María Gómez", "Age": 22, "ID": 1000640801, "Note": 3.8},
    1000640802: {"Name": "Juan Rodríguez", "Age": 19, "ID": 1000640802, "Note": 4.9},
    1000640803: {"Name": "Laura Torres", "Age": 21, "ID": 1000640803, "Note": 3.5},
    1000640804: {"Name": "Andrés Martínez", "Age": 23, "ID": 1000640804, "Note": 4.0}
}

menu = True  # Main loop control flag

while menu:
    # Menu options printed to user
    print("\033[93m\nBienvenido a la gestion de estudiantes\033[0m.")
    print("\033[93m\nOpciones que puede realizar\033[0m")
    print("\n1. Agregar estudiante.")
    print("2. Buscar estudiante.")
    print("3. Actualizar estudiante.")
    print("4. Eliminar estudiante.")
    print("5. Calcular promedio.")
    print("6. Salir.")

    option = int(input("\nIngrese la opción que desea realizar: "))

    # Check if the option is valid
    if option not in (1, 2, 3, 4, 5, 6):
        print("\033[91m\nOpción inválida. Por favor elige una opción entre 1 y 4.\033[0m")
        continue

    # Option 1: Add new student
    if option == 1:
        # Validate name
        while True:
            name = input("\nIngrese su nombre completo: ")
            if name.replace(" ", "").isalpha():
                break
            else:
                print("\n\033[91mEl nombre no puede contener numeros ni caracteres especiales.\033[0m")

        # Validate age
        while True:        
            age = input("\nIngrese su edad: ")
            if age.isdigit():
                age = int(age)
                break
            else:
                print("\033[91m\nLa edad no puede contener letras ni caracteres especiales\033[0m")

        # Validate ID
        while True:
            id = input("\nIngrese su documento de identidad: ")
            if id.isdigit():
                id = int(id)
                if id in students:
                    print("\033[91m\nEste documento ya está registrado. Intenta con otro.\033[0m")
                    continue
                else:
                    break
            else:
                print("\n\033[91mEl documento de identidad no puede contener letras ni caracteres especiales.\033[0m")   

        # Validate grade (note)
        while True:
            try:
                note = float(input("\nIngrese su nota (0.0-5.0): "))
                if 0.0 <= note <= 5.0:
                    break
                else:
                    print("\n\033[91mIngrese una nota válida entre 0.0 y 5.0\033[0m")
            except ValueError:
                print("\n\033[91mNo puede digitar letras, espacios en blanco ni caracteres especiales, digite un valor válido\033[0m")

        # Save student in dictionary
        students[id] = {
            "Name": name,
            "Age": age,
            "ID": id,
            "Note": note
        }
        print("\n\033[92mEstudiante agregado correctamente.\033[0m")

    # Option 2: Search student
    if option == 2:
        show_table = []
        # Display all students
        for i, (id, data) in enumerate(students.items()):
            show_table.append([data["Name"], data["Age"], data["ID"], data["Note"]])
        print(tabulate(show_table, headers=["Nombre", "Edad", "#Identificación", "Nota"], tablefmt="pretty"))

        # Ask user if they want to search
        while True: 
            search = input("\033[93m\n¿Deseas buscar un estudiante en específico?: S()si N()no: \033[0m").lower()
            if search == "s":
                # Search by ID or Name
                while True:
                    type_search = input("\033[93m\n¿Quieres buscar por su identificación (I) o por su nombre (N)?: \033[0m").lower()
                    if type_search == "i":
                        while True:
                            try:
                                search_id = int(input("\nIngrese el numero de identificacion que quiere buscar: "))
                                if search_id in students:
                                    data = students[search_id]
                                    print(tabulate([[data["Name"], data["Age"], data["ID"], data["Note"]]],
                                                   headers=["Nombre", "Edad", "#Identificación", "Nota"],
                                                   tablefmt="pretty"))
                                    break
                                else:
                                    print("\033[91m\nLa identificación ingresada no está registrada. Intenta de nuevo.\033[0m")
                            except ValueError:
                                print("\033[91m\nPor favor ingresa un número válido para el ID.\033[0m")
                        break 
                    elif type_search == "n":
                        while True:    
                            name_student = input("\nIngrese el nombre del estudiante que quiere buscar: ").lower()
                            found = False
                            for id, data in students.items():
                                if name_student in data["Name"].lower():
                                    print(tabulate([[data["Name"], data["Age"], data["ID"], data["Note"]]],
                                                   headers=["Nombre", "Edad", "#Identificación", "Nota"],
                                                   tablefmt="pretty"))
                                    found = True
                            if not found:
                                print("\033[91m\nNo se encontró ningún estudiante con ese nombre. Intenta nuevamente.\033[0m")
                            else:
                                break
                        break 
                    else:
                        print("\033[91m\nPor favor ingresa 'I' para Identificación o 'N' para nombre.\033[0m")

    # Option 3: Update student data
    if option == 3:
        while True:
            try:
                update_student = int(input("\nIngrese el número de identificación del estudiante que quiere actualizar: "))
                if update_student in students:
                    print(f"\033[93m\nActualizando estudiante: {students[update_student]['Name']}\033[0m")
                    update = False

                    # Update age
                    while True:
                        new_age = input("\nIngrese nueva edad del estudiante (Enter para dejar igual): ")
                        if new_age == "":
                            break
                        try:
                            age_u = int(new_age)
                            if age_u > 0:
                                students[update_student]["Age"] = age_u
                                update = True
                                break
                            else:
                                print("\033[91m\nNo se permiten valores negativos o cero para la edad.\033[0m")
                        except ValueError:
                            print("\033[91m\nEdad inválida. No puede digitar letras o caracteres especiales.\033[0m")

                    # Update grade
                    while True:
                        new_note = input("\nIngrese nueva nota (Enter para dejar igual): ")
                        if new_note == "":
                            break
                        try:
                            note_u = float(new_note)
                            if 0.0 <= note_u <= 5.0:
                                students[update_student]["Note"] = note_u
                                update = True
                                break
                            else:
                                print("\033[91m\nNota inválida. Debe estar entre 0.0 y 5.0.\033[0m")
                        except ValueError:
                            print("\033[91m\nNota inválida. No puede digitar letras o caracteres especiales.\033[0m")

                    if update:
                        print("\033[92m\nEstudiante actualizado correctamente.\033[0m")
                    else:
                        print("\033[93m\nNo se realizaron cambios.\033[0m")
                    break
                else:
                    print("\033[91m\nEl número de identificación ingresado no existe en la base de datos.\033[0m")
            except ValueError:
                print("\033[91m\nPor favor, ingrese un número válido para la identificación.\033[0m")

# eliminar estudiante
## validar estudante antes de, mensaje de confirmacion

# calcular promedio

## calcular todas las notas, se muestra con dos decimales

# listar estudiantes con notas menor de 3.0

