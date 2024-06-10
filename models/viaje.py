import json
from datetime import date
from models.gasto import Gasto
from models.tipo_pago import tipo_pago


class Viaje:

    def __init__(self, lugar_destino: str, fecha_inicio: date, fecha_final: date, presupuesto_diario: float):
        self._lugar_destino = lugar_destino
        self._fecha_inicio = fecha_inicio
        self._fecha_final = fecha_final
        self._presupuesto_diario = presupuesto_diario
        self._gastos = []

    def get_lugar_destino(self):
      return self._lugar_destino
    
    def get_fecha_inicio(self):
        return self._fecha_inicio
    
    def get_fecha_final(self):
        return self._fecha_final
    
    def get_presupuesto_diario(self):
        return self._presupuesto_diario
    
    def get_gastos(self):
        return self._gastos
    
    def set_lugar_destino(self, lugar_destino):
        self._lugar_destino = lugar_destino
    
    def set_fecha_inicio(self, fecha_inicio):
        self._fecha_inicio = fecha_inicio
    
    def set_fecha_final(self, fecha_final):
        self._fecha_final = fecha_final
    
    def set_presupuesto_diario(self, presupuesto_diario):
        self._presupuesto_diario = presupuesto_diario
    
    def set_gastos(self, gastos):
        self._gastos = gastos
    

    def agregar_gasto(self, fecha, valor, metodo_pago, tipo_gasto):
        if fecha < self._fecha_inicio or fecha > self._fecha_final:
            raise ValueError("La fecha del gasto no corresponde al rango del viaje")
        
        else:
            gasto = Gasto(fecha, valor, metodo_pago, tipo_gasto)
            gasto.pesos_cop(self._lugar_destino)
            self._gastos.append(gasto)
            gasto_total = 0

            for gasto in self._gastos:
                if fecha == gasto.get_fecha():
                    gasto_total += gasto.get_valor()

            diferencia = self._presupuesto_diario- gasto_total

            print("*"*40)
            print(f"{' GASTO ':^40}")
            print("*"*40)
            print(f"Fecha: {fecha}")
            print(f"Valor gasto: {gasto.get_valor():,} COP")
            print(f"Metodo de pago: {metodo_pago.name}")
            print(f"Tipo de gasto: {tipo_gasto.name}")
            print("*"*40)
            print(f"Presupuesto diario: {self._presupuesto_diario:,} COP")
            print(f"Total gastado en el dia: {gasto_total:,} COP")
            print(f"Presupuesto diario sobrante: {diferencia:,} COP")
            print("*"*40)
            print("\n")

            self._crear_json()

    def _crear_json(self):
        datos_viaje = {
            'destino': self._lugar_destino,
            'fecha inicio': self._fecha_inicio,
            'fecha fin': self._fecha_final,
            'presupuesto diario': self._presupuesto_diario,
            'gastos': []
        }

        for gasto in self._gastos:
            datos_viaje['gastos'].append({
                'fecha': gasto.get_fecha(),
                'tipo': str(gasto.get_tipo_gasto().name),
                'valor': gasto.get_valor(),
                'metodo pago': str(gasto.get_tipo_pago().name)
            })

        with open(f'Viaje_A_{self._lugar_destino}_De_{self._fecha_inicio}_Hasta_{self._fecha_final}.json', 'w', encoding='utf-8') as archivo:
            json.dump(datos_viaje, archivo, ensure_ascii=False, indent=4)
    
    def reporte_diario(self):
        reporte = {}
        for gasto in self._gastos:
            if gasto.get_fecha() not in reporte:
                reporte[gasto.get_fecha()] = {'efectivo': 0, 'tarjeta': 0, 'total': 0}
            if gasto.get_tipo_pago() == tipo_pago.EFECTIVO:
                reporte[gasto.get_fecha()]['efectivo'] += gasto.get_valor()
            else:
                reporte[gasto.get_fecha()]['tarjeta'] += gasto.get_valor()
            reporte[gasto.get_fecha()]['total'] += gasto.get_valor()
        return reporte




