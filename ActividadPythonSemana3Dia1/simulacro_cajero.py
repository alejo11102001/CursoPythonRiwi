saldo = []
menu = True
historial = [] 

while menu:
    print("\033[93m\nBienvenido a tu banco personal\033[0m.")
    print("\033[93m\nOpciones que puede realizar\033[0m")
    print("\n1. Ver saldo.")
    print("2. Retirar dinero.")
    print("3. Depositar dinero.")
    print("4. Ver historial de movimientos.")
    print("5. Salir.")

    opcion = int(input("\nIngrese la opción que desea realizar: "))

    while True:
        if opcion == 1:
            if len(saldo) == 0:
                print("\033[91m\nNo tiene saldo disponible\033[0m")
            else:
                total = sum(saldo)
                print(f"\033[96m\nTiene un saldo actual de {total} en su cuenta\033[0m")
            break

        elif opcion == 2:
            if len(saldo) == 0:
                print("\033[91m\nNo tiene saldo disponible para retirar\033[0m")
            else:
                while True:
                    retiro = input("\n¿Cuánto dinero desea retirar?: ")
                    retiro_Neto = float(retiro)
                    total = sum(saldo)
                    if retiro_Neto > total:
                        print("\033[91m\nFondos insuficientes.\033[0m")
                    else:
                        total = total - retiro_Neto
                        saldo = [total]
                        historial.append(("Retiro", retiro_Neto, total))
                        print("\033[92m\n¡El retiro ha sido exitoso!\033[0m")

                    continuar = input("\n¿Desea hacer otro retiro? s (SI) n (NO): ")
                    if continuar.lower() != "s":
                        break
            break

        elif opcion == 3:
            deposito = input("\n¿Cuánto dinero desea depositar?: ")
            monto = float(deposito)
            saldo.append(monto)
            total = sum(saldo)
            historial.append(("Depósito", monto, total))
            print("\033[92m\n¡El depósito ha sido exitoso!\033[0m")

            continuar = input("\n¿Desea hacer otro depósito? s (SI) n (NO): ")
            if continuar.lower() != "s":
                break

        elif opcion == 4:
            print("\nHistorial de movimientos:")
            if len(historial) == 0:
                print("\033[91m\nNo hay movimientos registrados.\033[0m")
            else:
                for tipo, monto, saldo_post in historial:
                    print(f"\n{tipo}: ${monto} | Saldo después: ${saldo_post}")
            break

        elif opcion == 5:
            print("\nGracias por usar el sistema.")
            menu = False
            break

        else:
            print("\nOpción no válida.")
            break