
# Sistema de Gestión de Estudiantes

Este programa en Python permite gestionar los registros de estudiantes, incluyendo agregar, buscar, actualizar y calcular promedios de notas. Utiliza una estructura de diccionario y la librería `tabulate` para mostrar los datos en forma de tabla.

## Cómo ejecutar el programa

1. Asegúrate de tener Python instalado (se recomienda versión 3.6 o superior).
2. Instala la librería `tabulate` si no la tienes:
   ```bash
   pip install tabulate
   ```
3. Ejecuta el script:
   ```bash
   python student_manager.py
   ```

## Ejemplos de entrada y salida

### Entrada:

- Selecciona la opción `1` para agregar un estudiante.
- Ingresa: `Nombre: Ana López`, `Edad: 21`, `ID: 1000640810`, `Nota: 4.6`

### Salida:
```
Estudiante agregado correctamente.
```

### Entrada:
- Selecciona la opción `2` para buscar.
- Elige buscar por nombre.
- Ingresa `Ana`.

### Salida:
```
+------------+------+------------------+------+
| Nombre     | Edad | #Identificación  | Nota |
+------------+------+------------------+------+
| Ana López  | 21   | 1000640810       | 4.6  |
+------------+------+------------------+------+
```

## Estructura del código

- `students`: Diccionario que almacena los datos de los estudiantes, utilizando el número de identificación como clave.
- `tabulate`: Librería utilizada para imprimir los datos en formato de tabla.
- Bucle principal: Muestra el menú y redirige la acción del usuario según su elección.
- Acciones disponibles:
  - **Agregar estudiante**: Valida los datos ingresados y registra un nuevo estudiante.
  - **Buscar estudiante**: Muestra todos los estudiantes y permite buscar por nombre o identificación.
  - **Actualizar estudiante**: Permite modificar la edad y la nota de un estudiante existente.
  - **(Por agregar)**: Eliminar estudiante, calcular promedio, listar estudiantes con nota inferior a cierto valor.

## Funcionalidades futuras

- Opción 4: Eliminar un estudiante.
- Opción 5: Calcular y mostrar el promedio de todas las notas.
- Opción 6: Salir del programa correctamente.
