from datetime import date
import requests
from models.tipo_pago import tipo_pago
from models.tipo_gasto import tipo_gasto


class Gasto:

    def __init__(self, fecha: date, valor: float, tipo_pago: tipo_pago, tipo_gasto: tipo_gasto):
        self._fecha = fecha
        self._valor = valor
        self._tipo_pago = tipo_pago
        self._tipo_gasto = tipo_gasto

    def get_valor(self):
        return self._valor

    def get_fecha(self):
        return self._fecha
    
    def get_tipo_pago(self):
        return self._tipo_pago
    
    def get_tipo_gasto(self):
        return self._tipo_gasto
    
    def set_valor(self, valor):
        self._valor = valor

    def set_fecha(self, fecha):
        self._fecha = fecha

    def set_tipo_pago(self, tipo_pago):
        self._tipo_pago = tipo_pago

    def set_tipo_gasto(self, tipo_gasto):
        self._tipo_gasto = tipo_gasto


    def pesos_cop(self, lugar_destino):  

        response = requests.get("https://csrng.net/csrng/csrng.php?min=3500&max=4500", timeout=5).json()

        if lugar_destino.upper() == "USA" or lugar_destino.upper() == "ESTADOS UNIDOS" or lugar_destino.upper() == "EEUU":
            self.set_valor(self._valor * response[0]['random'])

        if lugar_destino.upper() == 'Europa':
            self.set_valor(self._valor * response[0]['random'] + 200)

        if lugar_destino.upper() != "USA" and lugar_destino.upper() != "EEUU" and lugar_destino.upper() != "ESTADOS UNIDOS" and lugar_destino.upper() != "EUROPA":
            return

