from functions import *

def add_student():
    while True:
        id_input = input("\nIngrese su documento de identidad: ")
        if not id_input.isdigit():
            print("\033[91m\nEl documento debe ser un número válido, ni letras ni caracteres especiales.\033[0m")
            continue
        id = int(id_input)
        if id in students:
            print("\033[93m\nEl estudiante ya está registrado. Intente con otro documento.\033[0m")
            continue
        break
    while True:    
        full_name = input("\nIngrese su nombre completo: ").strip()
        if full_name.replace(" ", "").isalpha():
            break
        else:
            print("\033[91m\nEl nombre no debe contener numeros, ni caracteres especiales.\033[0m")
    while True:
        age_input = input("\nIngrese su edad: ")
        if age_input.isdigit():
            age = int(age_input)
            break
        else:
            print("\033[91m\nLa edad debe ser un número entero válido.\033[0m")
    while True:
        note_input = input("\nIngrese su nota (0.0-5.0): ")
        if note_input.replace(".", "", 1).isdigit() and note_input.count(".") <= 1:
            note = float(note_input)
            if 0.0 <= note <= 5.0:
                break
            else:
                print("\033[91m\nLa nota debe estar entre 0.0 y 5.0.\033[0m")
        else:
            print("\033[91m\nDebe ser una nota válida.\033[0m")
    add_student_function(id, full_name, age, note)

def search_student():
    while True:
        option_search = input("\n¿Desea buscar un estudiante por nombre o Id? i (ID) O n (NOMBRE): ").lower()
        if option_search == "":
            print("\033[91m\nEl campo no puede estar vacío. Por favor ingrésalo nuevamente.\033[0m")
            continue
        if option_search == "i":
            student_id = int(input("\nIngrese el ID del estudiante: "))
            search_student_id_function(student_id)
            break
        elif option_search == "n":
            student_name = input("\nIngrese el nombre del estudiante: ")
            search_student_name_function(student_name)
            break
        else:
            print("\033[91m\nOpción inválida. Debe ingresar 'i' para ID o 'n' para nombre.\033[0m")

def update_student():
    while True:
        student_update = input("\nIngrese el número de identificación del estudiante que quiere actualizar: ")
        if student_update == "":
            print("\033[91m\nEl Id no puede estar vacío. Por favor ingrésalo nuevamente.\033[0m")
            continue
        try:
            student_update = int(student_update)
        except ValueError:
            print("\033[91m\nEl ID debe ser un número entero.\033[0m")
            continue
        if student_update in students.keys():
            print(f"\033[93m\nActualizando estudiante: {students[student_update]['Full name']}\033[0m")
            update_student_function(student_update)
            break
        else:
            print("\033[93m\nEl estudiante no esta en la base de datos.\033[0m")

def delete_student():
    while True:
        delete_student = (int(input("\nDigite identificacion de usuario a eliminar: ")))
        if delete_student in students.keys():
            delete_student_function(delete_student)
            break
        else:
            print("\033[93m\nEl estudiante no esta en la base de datos.\033[0m")

while True:
        print("\033[93m\nBienvenido a la gestion de estudiantes\033[0m.")
        print("\033[93m\nOpciones que puede realizar\033[0m")
        print("\n1. Agregar estudiante.")
        print("2. Buscar estudiante.")
        print("3. Actualizar estudiante.")
        print("4. Eliminar estudiante.")
        print("5. Calcular promedio.")
        print("6. Lista de estudiantes reprobados.")
        print("7. Salir.")
        while True:
                try:
                    option = int(input("\n\033[96mElije la opción que deseas: \033[0m"))
                    if option < 1 or option > 7:
                        print("\n\033[93m\nIngrese una opción válida.\033[0m")
                        continue
                    break
                except ValueError:
                    print("\n\033[91mPor favor ingrese un número entre 1 y 7.\033[0m")
        match option:
            case 1:
                while True:
                    add_student()
                    if not advance_function_student():
                        break
            case 2:
                while True:
                    search_student()
                    if not advance_function_search():
                        break
            case 3:
                while True:
                    update_student()
                    if not advance_function_update():
                        break
            case 4:
                while True:
                    delete_student()
                    if not advance_function_remove():
                        break
            case 5:
                calculate_average_function()
                return_to_menu_or_exit()
            case 6:
                show_students_function()
                return_to_menu_or_exit()
            case 7:
                print("\033[93m\nSaliendo...\033[0m")
                print("\033[93m\nGracias Vuelva pronto\033[0m")
                exit()