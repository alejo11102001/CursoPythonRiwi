from tabulate import tabulate

# Datos de los usuarios
usuarios = {
    "1": {
        "nombre": "Daniel",
        "apellido": "Herrera",
        "contacto": {
            "correo": "garyford@gmail.com",
            "telefono": "001-512-801-0651x67779",
            "direccion": {
                "calle": "178 Walker Island Suite 840",
                "ciudad": "Gonzalezmouth",
                "estado": "Michigan",
                "codigo_postal": "92488",
                "pais": "Bermuda"
            }
        },
        "perfil": {
            "username": "bradley18",
            "fecha_nacimiento": "1987-07-15",
            "genero": "Masculino",
            "ocupacion": "Financial planner"
        },
        "redes_sociales": {
            "twitter": "https://twitter.com/mistytaylor",
            "linkedin": "https://linkedin.com/in/nancythomas",
            "instagram": ""
        },
        "preferencias": {
            "idioma": "Francés",
            "newsletter": True,
            "temas_interes": ["arte", "moda", "tecnología"]
        }
    },
    "2": {
        "nombre": "Joseph",
        "apellido": "Sullivan",
        "contacto": {
            "correo": "grussell@hotmail.com",
            "telefono": "006-305-4158x3659",
            "direccion": {
                "calle": "9638 Hawkins Crossing Apt. 914",
                "ciudad": "Robertchester",
                "estado": "Illinois",
                "codigo_postal": "28682",
                "pais": "Ethiopia"
            }
        },
        "perfil": {
            "username": "kennethtaylor",
            "fecha_nacimiento": "1981-03-26",
            "genero": "Otro",
            "ocupacion": "Clinical psychologist"
        },
        "redes_sociales": {
            "twitter": "https://twitter.com/claire15",
            "linkedin": "",
            "instagram": "https://instagram.com/kellycooper"
        },
        "preferencias": {
            "idioma": "Francés",
            "newsletter": False,
            "temas_interes": ["deportes", "arte", "viajes"]
        }
    },
    "3": {
        "nombre": "Kristina",
        "apellido": "Bradley",
        "contacto": {
            "correo": "mark58@hotmail.com",
            "telefono": "771-464-1767",
            "direccion": {
                "calle": "9396 Martin Bridge Apt. 544",
                "ciudad": "South Ryan",
                "estado": "Iowa",
                "codigo_postal": "41958",
                "pais": "Philippines"
            }
        },
        "perfil": {
            "username": "christine51",
            "fecha_nacimiento": "1966-09-21",
            "genero": "Femenino",
            "ocupacion": "Restaurant manager, fast food"
        },
        "redes_sociales": {
            "twitter": "https://twitter.com/dickersonjustin",
            "linkedin": "https://linkedin.com/in/michaela78",
            "instagram": ""
        },
        "preferencias": {
            "idioma": "Español",
            "newsletter": True,
            "temas_interes": ["cocina", "tecnología", "viajes"]
        }
    },
    "4": {
        "nombre": "Monica",
        "apellido": "Molina",
        "contacto": {
            "correo": "daniel59@yahoo.com",
            "telefono": "(925)185-9544x03157",
            "direccion": {
                "calle": "53484 Garrett Wall",
                "ciudad": "East Sherri",
                "estado": "Washington",
                "codigo_postal": "81748",
                "pais": "Syrian Arab Republic"
            }
        },
        "perfil": {
            "username": "kayla97",
            "fecha_nacimiento": "1987-11-19",
            "genero": "Femenino",
            "ocupacion": "Company secretary"
        },
        "redes_sociales": {
            "twitter": "https://twitter.com/rgomez",
            "linkedin": "",
            "instagram": "https://instagram.com/sarah44"
        },
        "preferencias": {
            "idioma": "Español",
            "newsletter": True,
            "temas_interes": ["viajes", "deportes", "tecnología"]
        }
    },
    "5": {
        "nombre": "Angela",
        "apellido": "House",
        "contacto": {
            "correo": "pwaters@dixon.biz",
            "telefono": "(616)639-1141",
            "direccion": {
                "calle": "8264 Morgan Lights",
                "ciudad": "Dianetown",
                "estado": "North Dakota",
                "codigo_postal": "64546",
                "pais": "Bolivia"
            }
        },
        "perfil": {
            "username": "randy13",
            "fecha_nacimiento": "2006-02-20",
            "genero": "Masculino",
            "ocupacion": "Airline pilot"
        },
        "redes_sociales": {
            "twitter": "",
            "linkedin": "https://linkedin.com/in/watkinsjessica",
            "instagram": "https://instagram.com/longlaura"
        },
        "preferencias": {
            "idioma": "Inglés",
            "newsletter": False,
            "temas_interes": ["moda", "arte", "cocina"]
        }
    }
}

from tabulate import tabulate

# Colores ANSI
RESET = "\033[0m"
ROJO = "\033[91m"
COLORES_FILA = [
    "\033[96m",  # Cian
    "\033[92m",  # Verde
    "\033[95m",  # Magenta
    "\033[93m",  # Amarillo
    "\033[94m",  # Azul
]

# Función para colorear texto vacío
def mostrar_valor(valor):
    if not valor:
        return f"{ROJO}no tiene{RESET}"
    return valor

# Preparar los datos para la tabla
tabla = []
for i, usuario in enumerate(usuarios.values()):
    color = COLORES_FILA[i % len(COLORES_FILA)]

    nombre = mostrar_valor(usuario['nombre'])
    apellido = mostrar_valor(usuario['apellido'])
    correo = mostrar_valor(usuario['contacto']['correo'])
    telefono = mostrar_valor(usuario['contacto']['telefono'])

    direccion = usuario['contacto']['direccion']
    direccion_completa = f"{mostrar_valor(direccion['calle'])}, {mostrar_valor(direccion['ciudad'])}, {mostrar_valor(direccion['estado'])}, {mostrar_valor(direccion['codigo_postal'])}, {mostrar_valor(direccion['pais'])}"

    perfil = usuario['perfil']
    fecha_nacimiento = mostrar_valor(perfil['fecha_nacimiento'])
    genero = mostrar_valor(perfil['genero'])
    ocupacion = mostrar_valor(perfil['ocupacion'])

    redes = usuario['redes_sociales']
    redes_sociales = (
        f"Twitter: {mostrar_valor(redes.get('twitter'))}, "
        f"LinkedIn: {mostrar_valor(redes.get('linkedin'))}, "
        f"Instagram: {mostrar_valor(redes.get('instagram'))}"
    )

    preferencias = usuario['preferencias']
    idioma = mostrar_valor(preferencias['idioma'])
    newsletter = "Sí" if preferencias['newsletter'] else "No"
    temas_interes = mostrar_valor(", ".join(preferencias['temas_interes']))

    fila = [nombre, apellido, correo, telefono, direccion_completa,
            fecha_nacimiento, genero, ocupacion, redes_sociales, idioma, newsletter, temas_interes]

    # Aplicar color a toda la fila
    fila_coloreada = [f"{color}{campo}{RESET}" for campo in fila]
    tabla.append(fila_coloreada)

# Encabezados
headers = ["Nombre", "Apellido", "Correo", "Teléfono", "Dirección",
           "Fecha Nacimiento", "Género", "Ocupación", "Redes Sociales", "Idioma", "Newsletter", "Temas de Interés"]

# Mostrar tabla con formato bonito
print(tabulate(tabla, headers=headers, tablefmt="fancy_grid"))
