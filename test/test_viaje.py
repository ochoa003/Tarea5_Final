import unittest
from models.viaje import Viaje
from models.tipo_pago import tipo_pago
from models.tipo_gasto import tipo_gasto

class TestViaje(unittest.TestCase):

    # Test para verificar que se pueda agregar un gasto local a un viaje
    def test_agregar_gasto_local(self):
        viaje = Viaje("COLOMBIA", "2022-06-10", "2022-06-16", 100000)
        viaje.agregar_gasto("2022-06-10", 10000, tipo_pago.EFECTIVO, tipo_gasto.ALIMENTACION)

        self.assertEqual(viaje.get_gastos()[0].get_valor(), 10000)

    # Test para verificar que se pueda agregar un gasto internacional a un viaje
    def test_agregar_gasto_internacional(self):
        viaje = Viaje("EEUU", "2022-06-10", "2022-06-16", 100000)
        viaje.agregar_gasto("2026-06-10", 22, tipo_pago.EFECTIVO, tipo_gasto.ALIMENTACION)

        self.assertNotEqual(viaje.get_gastos()[0].get_valor(), 22)

    # Test para verificar que se realice el reporte diario de un viaje local
    def test_agregar_gasto_con_fecha_menor_inicial(self):
        viaje = Viaje('Estados Unidos', '2022-06-10', '2022-06-16', 1000000)
        with self.assertRaises(ValueError):
            viaje.agregar_gasto('2022-06-09', 100, tipo_pago.TARJETA, tipo_gasto.ALIMENTACION)

if __name__ == '__main__':
    unittest.main()

