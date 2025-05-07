import random
import string

# NIVEL BASICO

def saludar():
    nombre = input("Ingrese su nombre: ")
    print(f"¡Hola {nombre} ten un gran dia")

def suma():
    numero1 = int(input("Ingrese numero 1: "))
    numero2 = int(input("Ingrese numero 2: "))
    resultado = numero1 + numero2
    print(resultado)

def par_impar():
    num = int(input("Ingrese numero: "))
    if num % 2 == 0:
        print(f"El numero {num} es par")
    else:
        print(f"El numero {num} es impar")

def mayoria_edad():
    edad = int(input("Ingrese su edad: "))
    if edad < 18:
        print("Es menor de edad")
    else:
        print("Es mayor de edad")

def conversion():
    temp = float(input("Ingrese temperatura en Celsius: "))
    conver = (temp * 9/5) + 32
    print(f"{temp} en Fahrenhei son es: {conver}")

def area_tri():
    base = float(input("Ingrese la base del triangulo: "))
    altura = float(input("Ingrese la altura del triangulo: "))
    resultado = (base * altura) / 2
    print(f"El area del triangulo es: {resultado}")

def mostrar_mayor():
    entrada = input("Ingresa una lista de números separados por coma: ")
    lista = entrada.split(",")
    lista = [int(n) for n in lista]
    mayor = max(lista)
    print("El número mayor es:", mayor)

def letra_palabras():
    entrada = input("Ingrese palabra: ")
    print(f"La cantidad de a en la palabra son: {entrada.count("a")}")

# NIVEL INTERMEDIO

def filtrar_pares():
    entrada = input("Ingresa una lista de números separados por coma: ")
    lista = entrada.split(",")
    #nueva_lista = []
    #for n in lista:
    #    nueva_lista.append(int(n))
    #lista = nueva_lista
    lista = [int(n) for n in lista]
    #pares = []
    #for n in lista:
    #    if n % 2 == 0:
    #        pares.append(n)
    pares = [n for n in lista if n % 2 == 0]
    print("Los números pares son:", pares)

def es_palindromo():
    texto = input("Ingresa una palabra o frase: ")
    texto = texto.lower().replace(" ", "")
    if texto == texto[::-1]:
        print("Es un palíndromo.")
    else:
        print("No es un palíndromo.")

def factorial():
    n = int(input("Ingresa un número: "))
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    print(f"El factorial de {n} es: {resultado}")

def repetidos():
    entrada = input("Ingrese elementos separados por coma: ")
    lista = entrada.split(",")
    sin_duplicados = list(set(lista))
    print("La nueva lista sin repetidos:", sin_duplicados)

def fizzbuzz():
    num = int(input("Ingresa un número: "))
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

def vocales():
    entrada = input("Ingrese texto: ")
    entrada = entrada.lower()
    contador = 0
    for letra in entrada:
        if letra in "aeiou":
            contador += 1
    print("La cantidad de vocales es:", contador)

def invertir_texto():
    texto = input("Ingresa una palabra o frase que desee invertir: ")
    texto = texto.lower().replace(" ", "")
    print(texto[::-1])

# NIVEL DIFICIL

def validar_contraseña():
    contraseña = input("Ingresa una contraseña segura: ")

    tiene_mayuscula = any(c.isupper() for c in contraseña)
    tiene_minuscula = any(c.islower() for c in contraseña)
    tiene_numero = any(c.isdigit() for c in contraseña)
    tiene_simbolo = any(not c.isalnum() for c in contraseña)

    if tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_simbolo:
        print("Contraseña segura")
    else:
        print("Contraseña insegura, Debe tener mayúsculas, minúsculas, números y símbolos.")

def dado():
    inicio = input("Digite 'inicio' para rodar el dado: ")
    if inicio == 'inicio':
        numero = random.randint(1,6)
        print(numero)

def suma_unicos():
    entrada = input("Ingresa números separados por coma: ")
    lista = [int(n) for n in entrada.split(",")]
    suma = sum(n for n in lista if lista.count(n) == 1)
    print("La suma de elementos únicos es:", suma)

def generar_contraseña():
    inicio = input("Digite 'iniciar' para establecer tu clave: ")
    if inicio == 'iniciar':
        contraseña = ''.join(random.choices(string.printable, k=7))
        print("Tu contraseña generada es:", contraseña)

def composicion(f, g, x):
    print(f(g(x)))

def a_mayusculas(texto):
    return texto.upper()

def añadir_signos(texto):
    return "¡" + texto + "!"



