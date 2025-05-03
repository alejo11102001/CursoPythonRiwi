# Sistema de Gestión y Costeo de Equipaje Aéreo

Este proyecto es un sistema básico para registrar la compra de boletos de avión, calcular costos por equipaje y generar reportes.

## Funcionalidad

- Registra pasajeros, tipo de viaje y peso del equipaje.
- Calcula el costo total del viaje (boleto + equipaje).
- Genera un ID único por compra.
- Muestra un resumen con todos los datos ingresados.

## Tipos de Viaje y Costos

**Viajes:**

- Bogotá → Medellín: $230.000  
- Bogotá → España: $4.200.000  

**Equipaje Principal:**

- Hasta 20 kg: $50.000  
- Hasta 30 kg: $70.000  
- Hasta 50 kg: $110.000  
- Más de 50 kg: No permitido  

**Equipaje de Mano:**

- Máximo 13 kg  
- Si se pasa, se rechaza, pero el pasajero puede viajar igual.

## Datos que muestra por reserva

- ID de compra  
- Nombre  
- Destino y fecha  
- Estado del equipaje  
- Total a pagar  

## Reporte para el administrador

- Total recaudado  
- Total por fecha  
- Pasajeros procesados  
- Pasajeros por tipo de viaje  
- Consultar compra por ID  
