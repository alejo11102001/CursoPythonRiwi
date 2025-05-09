# Sistema de Gestión de Estudiantes

Este es un sistema simple de gestión de estudiantes que permite realizar varias operaciones sobre los registros de estudiantes, como agregar, buscar, actualizar, eliminar y calcular el promedio de notas. También permite mostrar una lista de estudiantes que están reprobados.

## Requisitos

Para ejecutar este proyecto, asegúrate de tener instalado Python y la biblioteca `tabulate` para una visualización en forma de tabla. Puedes instalarla con:

```bash
pip install tabulate
```

## Archivos del Proyecto

- **`inventary_index.py`**: Este es el archivo principal que contiene el menú de opciones y coordina las interacciones con el usuario.
- **`functions.py`**: Contiene las funciones que realizan las operaciones sobre los estudiantes, como agregar, buscar, actualizar, eliminar y calcular el promedio.

## Funcionalidades

### 1. **Agregar estudiante**
Permite agregar un nuevo estudiante con su documento de identidad, nombre completo, edad y nota. Asegura que los datos ingresados sean válidos.

### 2. **Buscar estudiante**
Permite buscar un estudiante por su ID o su nombre. El sistema mostrará la información del estudiante correspondiente.

### 3. **Actualizar estudiante**
Permite actualizar la edad y la nota de un estudiante, manteniendo los demás datos intactos.

### 4. **Eliminar estudiante**
Permite eliminar un estudiante del sistema mediante su ID.

### 5. **Calcular promedio**
Calcula y muestra el promedio de las notas de todos los estudiantes registrados.

### 6. **Lista de estudiantes reprobados**
Muestra una lista de los estudiantes cuya nota es inferior a 3.0.

### 7. **Salir**
Sale del sistema y termina la ejecución.

## Ejemplo de Uso

Al ejecutar el archivo `inventary_index.py`, el sistema te presentará un menú con varias opciones. Por ejemplo:

```bash
Bienvenido a la gestion de estudiantes.

Opciones que puede realizar

1. Agregar estudiante.
2. Buscar estudiante.
3. Actualizar estudiante.
4. Eliminar estudiante.
5. Calcular promedio.
6. Lista de estudiantes reprobados.
7. Salir.
```

Elige una opción introduciendo el número correspondiente. Si seleccionas la opción 1 para agregar un estudiante, el sistema te pedirá la información necesaria y realizará las validaciones correspondientes.

## Notas

- El sistema utiliza un diccionario `students` para almacenar los estudiantes, donde la clave es el documento de identidad y el valor es otro diccionario con el nombre, la edad y la nota.
- Las validaciones aseguran que la información ingresada sea correcta (por ejemplo, las notas deben estar entre 0.0 y 5.0).
