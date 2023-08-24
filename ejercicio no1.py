def calcular_tarifa_estacionamiento(horas, minutos, dia):
    tarifas = {"lunes": 2.00, "martes": 2.00, "miércoles": 2.00,
               "jueves": 2.50, "viernes": 2.50,
               "sábado": 3.00, "domingo": 3.00}

    tarifa_hora = tarifas.get(dia, None)

    if tarifa_hora is None:
        print("Día de la semana incorrecto")
        return

    tiempo_total = horas + minutos / 60

    if minutos % 5 != 0:
        tiempo_total = round(tiempo_total) + 1

    total_pagar = tarifa_hora * tiempo_total
    print(f"Total a pagar: ${total_pagar:.2f}")

# Entrada de datos
horas_estacionadas = int(input("Ingrese las horas estacionadas: "))
minutos_estacionados = int(input("Ingrese los minutos estacionados: "))
dia_semana = input("Ingrese el día de la semana: ").lower()

calcular_tarifa_estacionamiento(horas_estacionadas, minutos_estacionados, dia_semana)


