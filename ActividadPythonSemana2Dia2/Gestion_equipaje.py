boletas = {}
boleto = 1
opcion = ""

while opcion != "5":
    print("\n=== Menú Principal ===")
    print("1. Registrar nuevo boleto")
    print("2. Ver resumen de todos los boletos")
    print("3. Generar informe administrativo")
    print("4. Consultar compra por ID")
    print("5. Salir")
    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        continuar_registro = True
        while continuar_registro:
            print("\n--- Registro de Boleto ---")

            nombre = input("\nDigite su nombre completo: ").strip()
            while not nombre:
                nombre = input("Nombre no válido. Intente de nuevo: ").strip()

            tipo_viaje = input("\nDigite tipo de viaje ('nacional' o 'internacional'): ").lower()
            while tipo_viaje not in ["nacional", "internacional"]:
                tipo_viaje = input("Tipo inválido. Escriba 'nacional' o 'internacional': ").lower()

            if tipo_viaje == "nacional":
                costo = 230000
                print("\nCosto del viaje: $230.000")
            else:
                costo = 4200000
                print("\nCosto del viaje: $4.200.000")

            while True:
                try:
                    peso_equipaje = float(input("\nDigite peso del equipaje (Kg): "))
                    if peso_equipaje > 50:
                        print("Equipaje no admitido (debe cancelar o viajar sin equipaje)")
                        continuar_viaje = input("¿Desea continuar sin equipaje? (si/no): ").lower()
                        if continuar_viaje == "si":
                            costo_e = 0
                            break
                        else:
                            costo_e = 0
                            break
                    elif peso_equipaje <= 20:
                        costo_e = 50000
                        print("\nCosto adicional: $50.000")
                        break
                    elif peso_equipaje <= 30:
                        costo_e = 70000
                        print("\nCosto adicional: $70.000")
                        break
                    elif peso_equipaje <= 50:
                        costo_e = 110000
                        print("\nCosto adicional: $110.000")
                        break
                except ValueError:
                    print("Por favor, ingrese un número válido.")

            equipaje_mano = input("\n¿Lleva equipaje de mano? (si/no): ").lower()
            estado_mano = "No lleva equipaje de mano"
            if equipaje_mano == "si":
                try:
                    mano_peso = float(input("Digite el peso del equipaje de mano (Kg): "))
                    if mano_peso > 13:
                        estado_mano = "Equipaje de mano rechazado (excede 13kg)"
                    else:
                        estado_mano = "Equipaje de mano aceptado"
                except ValueError:
                    estado_mano = "Respuesta inválida para peso"
            elif equipaje_mano != "no":
                estado_mano = "Respuesta inválida"

            fecha_viaje = input("\nDigite la fecha del viaje (DD/MM/AAAA): ").strip()
            while not fecha_viaje:
                fecha_viaje = input("Fecha inválida. Intente de nuevo: ").strip()

            costo_total = costo + costo_e
            boleto_id = f"COMP{boleto:04}"
            boleto += 1

            boletas[boleto_id] = {
                "Nombre": nombre,
                "Tipo de viaje": tipo_viaje,
                "Fecha de viaje": fecha_viaje,
                "Peso del equipaje": peso_equipaje,
                "Equipaje de mano": estado_mano,
                "Costo boleto": costo_total
            }

            print("\n¡Boleto agregado exitosamente!")

            seguir = input("\n¿Desea registrar otro boleto? (si/no): ").lower()
            if seguir != "si":
                continuar_registro = False

    elif opcion == "2":
        if boletas:
            print("\n--- Resumen de Pasajeros ---")
            for id_boleto, datos in boletas.items():
                print(f"\nID: {id_boleto}")
                for clave, valor in datos.items():
                    print(f"{clave}: {valor}")
        else:
            print("\nNo hay boletos registrados.")

    elif opcion == "3":
        print("\n--- Informe Administrativo ---")
        print("1. Ver total recaudado")
        print("2. Ver número de pasajeros (total / nacional / internacional)")
        print("3. Buscar recaudo por fecha")
        subopcion = input("Seleccione una subopción (1/2/3): ")

        if subopcion == "1":
            total_general = sum(datos["Costo boleto"] for datos in boletas.values())
            print(f"\nTotal recaudado por boletos: ${total_general:,.0f}")

        elif subopcion == "2":
            total_pasajeros = len(boletas)
            nacionales = sum(1 for datos in boletas.values() if datos["Tipo de viaje"] == "nacional")
            internacionales = sum(1 for datos in boletas.values() if datos["Tipo de viaje"] == "internacional")
            print(f"\nTotal de pasajeros: {total_pasajeros}")
            print(f"Nacionales: {nacionales}")
            print(f"Internacionales: {internacionales}")

        elif subopcion == "3":
            fecha_consulta = input("\nIngrese una fecha para consultar (DD/MM/AAAA): ").strip()
            total_fecha = sum(datos["Costo boleto"] for datos in boletas.values() if datos["Fecha de viaje"] == fecha_consulta)
            print(f"Total recaudado el {fecha_consulta}: ${total_fecha:,.0f}")
        else:
            print("Subopción no válida.")

    elif opcion == "4":
        buscar_id = input("\nIngrese el ID de una compra (ej: COMP0003): ").strip()
        if buscar_id in boletas:
            print(f"\nDetalles del boleto {buscar_id}:")
            for clave, valor in boletas[buscar_id].items():
                print(f"{clave}: {valor}")
        else:
            print("ID no encontrado.")

    elif opcion == "5":
        print("\nSaliendo del sistema. Gracias por usarlo.")
    else:
        print("\nOpción no válida. Intente de nuevo.")