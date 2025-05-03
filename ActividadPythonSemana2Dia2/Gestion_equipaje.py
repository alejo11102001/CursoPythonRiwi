### Entradas:

# nombre

## destino (tipo de viaje)
# bogota -> medellin (Nacional) 230.000
# bogota -> españa (internacional) 4.200.000

## equipaje (principal)
# Hasta 20 kg	$50.000
# Hasta 30 kg	$70.000
# Hasta 50 kg	$110.000
# Más de 50 kg	❌ No admitido (debe cancelar o viajar sin equipaje
# lleva equipaje de mano ? SI -NO 
# if equipaje_mano > 13: rechazado el equipaje

## Fecha de vuelo

## calcular el costo total del viaje

## asignar id unico
## limites de peso
## aplicar costos por equipaje
## resumen
continuar = True
boletas = []
while continuar:
    nombre = input("\nDigite su nombre completo: ")

    tipo_viaje = input("\nDigite tipo de viaje (nacional o internacional): ")
    if tipo_viaje == "nacional":
        costo = 230000
        print("\nCosto del viaje $230.000")
    elif tipo_viaje == "internacional":
        costo = 4200000
        print("\nCosto del viaje $4.200.000")
    else:
        print("\nViaje no disponible")

    peso_equipaje = float(input("\nDigite peso del equipaje (Kg): "))
    if peso_equipaje <= 20: 
        costo_e = 50000
        print("\nCosto adicional de $50.000")
    elif peso_equipaje > 20 and peso_equipaje <= 30:
        costo_e = 70000
        print("\nCosto adicional de $70.000")
    elif peso_equipaje > 30 and peso_equipaje <= 50:
        costo_e = 110000
        print("\nCosto adicional de $110.000")
    else:
        print("\nNo admitido (debe cancelar o viajar sin equipaje)")

    equipaje_mano = input("\n¿Lleva equipaje de mano? (si) o (no): ")
    estado_mano = "No lleva equipaje de mano"

    if equipaje_mano.lower() == "si":
            mano_peso = float(input("\nDigite el peso del equipaje de mano (Kg): "))
            if mano_peso > 13:
                estado_mano = "\nEquipaje de mano rechazado"
            else:
                estado_mano = "\nEquipaje de mano aceptado"
    elif equipaje_mano.lower() == "no":
        estado_mano = "\nNo lleva equipaje de mano"
    else:
        estado_mano = "\nRespuesta inválida"

    fecha_viaje = input("\nDigite la fecha del viaje: ")

    costo_total = costo + costo_e

    boleta = [nombre, tipo_viaje, fecha_viaje, peso_equipaje, estado_mano, costo_total]
    boletas.append(boleta)
    print("\033[92m\n¡Boleto agregado exitosamente!\033[0m")

    seguir = input("\nDesea comprar otro boleto (si) o (no): ")
    if seguir == "si":
        continue
    else:
        break


print("\nResumen del Pasajero:")
print(boletas)

for suma in boletas:
    boletas[suma] = costo_total
    suma_total += suma

print(suma_total)