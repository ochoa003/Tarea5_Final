import time
from models.viaje import Viaje
from models.gasto import Gasto
from models.tipo_gasto import tipo_gasto
from models.tipo_pago import tipo_pago

viaje = Viaje("USA", "2022-06-10", "2022-06-16", 1000000)

viaje.agregar_gasto("2022-06-10", 10,tipo_pago.EFECTIVO, tipo_gasto.ALIMENTACION)
time.sleep(3)  # Espera de 3 segundos
viaje.agregar_gasto("2022-06-10", 20,tipo_pago.TARJETA, tipo_gasto.ENTRETENIMIENTO)
time.sleep(3)  # Espera de 3 segundos
viaje.agregar_gasto("2022-06-11", 20,tipo_pago.TARJETA, tipo_gasto.ALOJAMIENTO)

for reporte in viaje.reporte_diario():
    print(reporte + " Efectivo: " + str(viaje.reporte_diario()[reporte]["efectivo"]) + " Tarjeta: " + str(viaje.reporte_diario()[reporte]["tarjeta"]) + " Total: " + str(viaje.reporte_diario()[reporte]["total"]) + "\n")
