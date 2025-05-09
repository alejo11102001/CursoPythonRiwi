from tabulate import tabulate

students = {
    1000640800: {"Full name": "Carlos Perez", "Age": 20, "Note": 4.2},
    1000640801: {"Full name": "Maria Gomez", "Age": 22, "Note": 3.8},
    1000640802: {"Full name": "Juan Rodriguez", "Age": 19, "Note": 4.9},
    1000640803: {"Full name": "Laura Torres", "Age": 21, "Note": 2.9},
    1000640804: {"Full name": "Andres Martinez", "Age": 23, "Note": 2.5}
}

def add_student_function(id, full_name, age, note):
    students[id] = {
        "Full name": full_name,  
        "Age": age,
        "Note": note
    }
    print(f"\033[92m\nEstudiante '{full_name}' agregado correctamente.\033[0m")

def search_student_id_function(search_student_id):
    while True:
        if search_student_id in students.keys():
            data_students = students[search_student_id]
            table = [[
                f"\033[94m{search_student_id}\033[0m",
                f"\033[93m{data_students['Full name']}\033[0m", 
                f"\033[92m{data_students['Age']}\033[0m", 
                f"\033[92m{data_students['Note']}\033[0m" 
            ]]
            print("\n\033[96mEstudiante encontrado:\033[0m")
            print(tabulate(table, headers=["\033[95mID\033[0m", "\033[95mNombre completo\033[0m", "\033[95mEdad\033[0m", "\033[95mNota\033[0m"], tablefmt="pretty"))
            break
        else:
            print("\n\033[93mNo se encontró un estudiante con ese ID.\033[0m")
        break

def search_student_name_function(search_student_name):
    fount = False
    for id, data_students in students.items():
        if search_student_name.lower() in data_students["Full name"].lower():
            table = [[
                f"\033[94m{id}\033[0m",
                f"\033[93m{data_students['Full name']}\033[0m", 
                f"\033[92m{data_students['Age']}\033[0m",
                f"\033[92m{data_students['Note']}\033[0m" 
            ]]
            print("\n\033[96mEstudiante encontrado:\033[0m")
            print(tabulate(table, headers=["\033[95mID\033[0m", "\033[95mNombre completo\033[0m", "\033[95mEdad\033[0m", "\033[95mNota\033[0m"], tablefmt="pretty"))
            fount = True
            break
    if not fount:
        print("\033[93m\nNo se encontró ningún estudiante con ese nombre.\033[0m")

def update_student_function(student_update):
    update = False

    while True:
        new_age = input("\nIngrese nueva edad del estudiante (Enter para dejar igual): ")
        if new_age == "":
            break
        try:
            age_u = int(new_age)
            if age_u > 0:
                students[student_update]["Age"] = age_u
                update = True
                break
            else:
                print("\033[91m\nEdad inválida. No se permiten valores negativos o cero.\033[0m")
        except ValueError:
            print("\033[91m\nEdad inválida. Debe ser un número entero.\033[0m")
    while True:
        new_note = input("\nIngrese nueva nota del estudiante (Enter para dejar igual): ")
        if new_note == "":
            break
        try:
            note_u = float(new_note)
            if 0.0 <= note_u <= 5.0:
                students[student_update]["Note"] = note_u
                update = True
                break
            else:
                print("\033[91m\nNota inválida. Debe estar entre 0.0 y 5.0.\033[0m")
        except ValueError:
            print("\033[91m\nNota inválida. Debe ser un número decimal.\033[0m")
    if update:
        print(f"\033[92m\nEstudiante {students[student_update]['Full name']} actualizado correctamente.\033[0m")
    else:
        print("\033[93m\nNo se realizaron cambios.\033[0m")

def delete_student_function(delete_student):
    if delete_student in students:
        name = students[delete_student]['Full name']
        students.pop(delete_student)
    print(f"\033[92m\nEstudiante {name} eliminado correctamente.\033[0m")

def calculate_average_function():
    counter = 0
    total_notes = 0.0
    for student in students.values():
        counter += 1
        total_notes += student["Note"]
    average = total_notes / counter
    print((f"\033[94m\nEl promedio de notas es: {average:.2f}\033[0m"))

def show_students_function():
    failing_students = [] 
    for student in students.values():
        if student["Note"] < 3.0:
            failing_students.append([student["Full name"], student["Note"]])

    if failing_students:
        print("\n\033[91mEstudiantes que están perdiendo:\033[0m")
        print(tabulate(failing_students, headers=["Nombre", "Nota"], tablefmt="pretty"))
    else:
        print("\n\033[92mNingún estudiante está perdiendo actualmente.\033[0m")

def return_to_menu_or_exit():
    while True:
        option_out = input("\033[93m\n¿Deseas volver al menú inicial?: S()si N()no:\033[0m")
        if option_out == "s":
            return False 
        elif option_out == "n":
            print("\033[93m\nSaliendo del sistema...\033[0m")
            exit()
        else:
            print("\033[91m\nPor favor ingresa 'N' para no o 'S' para sí.\033[0m")

def advance_function_student():
    while True:
        output_menu = input("\033[93m\n¿Deseas continuar ingresando estudiantes?: S()si N()no:\033[0m")
        if output_menu == "n":
            return return_to_menu_or_exit() 
        elif output_menu == "s":
            return True 
        else:
            print("\033[91m\nPor favor ingresa 'N' para no o 'S' para sí.\033[0m")

def advance_function_search():
    while True:
        search_again = input("\033[93m\n¿Deseas buscar otro estudiante?: S()si N()no: \033[0m")
        if search_again == "n":
            return return_to_menu_or_exit()
        elif search_again == "s":
            return True
        else:
            print("\033[91m\nPor favor ingresa 'N' para no o 'S' para sí.\033[0m")

def advance_function_update():
    while True:
        output_update = input("\033[93m\n¿Deseas actualizar otro estudiante? S(si) N(no): \033[0m")
        if output_update == "n":
            return return_to_menu_or_exit()
        elif output_update == "s":
            return True
        else:
            print("\033[91m\nPor favor ingresa 'N' para no o 'S' para sí.\033[0m")

def advance_function_remove():
    while True:
        output_remove = input("\033[93m\n¿Deseas eliminar otro estudiante? S(si) N(no): \033[0m")
        if output_remove == "n":
            return return_to_menu_or_exit()
        elif output_remove == "s":
            return True
        else:
            print("\033[91m\nPor favor ingresa 'N' para no o 'S' para sí.\033[0m")