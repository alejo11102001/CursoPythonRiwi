# Sistema de Agenda de Contactos y Registro de Libros

Este repositorio contiene dos sistemas:
1. **Sistema de Agenda de Contactos**: Permite gestionar contactos con funcionalidades como agregar, mostrar, actualizar y eliminar.
2. **Sistema de Registro de Libros**: Permite gestionar un catálogo de libros con funcionalidades como agregar, mostrar, actualizar y eliminar libros.

## Funcionalidades

### Agenda de Contactos

1. **Agregar Contacto**: Añadir nuevos contactos con:
   - Nombre (solo letras y espacios)
   - Teléfono (solo números)
   - Correo electrónico (formato válido y único)

2. **Mostrar Listado de Contactos**: Ver todos los contactos registrados en formato de tabla.

3. **Actualizar Contacto**: Actualizar datos de un contacto seleccionando su ID. Los datos que se pueden actualizar son:
   - Nombre
   - Teléfono
   - Correo electrónico

4. **Eliminar Contacto**: Eliminar un contacto seleccionando su ID con confirmación.

### Registro de Libros

1. **Agregar Libro**: Añadir nuevos libros con:
   - Título
   - Autor
   - Año de publicación
   - ISBN

2. **Mostrar Listado de Libros**: Ver todos los libros registrados en formato de tabla.

3. **Actualizar Libro**: Actualizar los datos de un libro seleccionando su ID. Se pueden actualizar:
   - Título
   - Autor
   - Año de publicación
   - ISBN

4. **Eliminar Libro**: Eliminar un libro seleccionando su ID con confirmación.

## Requisitos

Este programa requiere Python 3.x y la librería `tabulate`. Instálala con:

```bash
pip install tabulate
