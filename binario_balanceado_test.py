import unittest

# Se importa el código a testear.
from binario_balanceado import decimal_a_binario, es_binario_balanceado, \
                      cantidad_binarios_balanceados_entre, siguiente_binario_balanceado, \
                      anterior_binario_balanceado, binario_balanceado_mas_cercano

#####################################################################

class TestBinariosBalanceados(unittest.TestCase):
    def test_decimal_a_binario(self):
        self.assertTrue(decimal_a_binario(2),10)
        self.assertTrue(decimal_a_binario(20),10100)
        self.assertEqual(decimal_a_binario(120), "1111000")
        self.assertEqual(decimal_a_binario(2), "10")
        self.assertNotEqual(decimal_a_binario(20), "11")
        self.assertNotEqual(decimal_a_binario(20), "abc")

    def test_es_binario_balanceado(self):
        self.assertTrue(es_binario_balanceado(2))
        self.assertTrue(es_binario_balanceado(10))
        self.assertEqual(es_binario_balanceado(20), False)
        self.assertEqual(es_binario_balanceado(3), False)
        self.assertFalse(es_binario_balanceado(3), False)
        self.assertFalse(es_binario_balanceado(100), False)
        self.assertNotEqual(es_binario_balanceado(100), 4)
        self.assertNotEqual(es_binario_balanceado(6), 5)
        
    def test_cantidad_binarios_balanceados_entre(self):
        self.assertEqual(cantidad_binarios_balanceados_entre(1 , 4), 1)
        self.assertEqual(cantidad_binarios_balanceados_entre(4 , 10), 2)
        self.assertTrue(cantidad_binarios_balanceados_entre(1 , 3), 1) 
        self.assertTrue(cantidad_binarios_balanceados_entre(8 , 10), 2) 
        self.assertNotEqual(cantidad_binarios_balanceados_entre(8 , 10), 3) 
        self.assertNotEqual(cantidad_binarios_balanceados_entre(1 , 3), 2) 
       
    def test_siguiente_binario_balanceado(self):
        self.assertEqual(siguiente_binario_balanceado(1),2) 
        self.assertEqual (siguiente_binario_balanceado(3),9)
        self.assertTrue(siguiente_binario_balanceado(1),2) 
        self.assertTrue(siguiente_binario_balanceado(9),10) 
        self.assertNotEqual(siguiente_binario_balanceado(1),3) 
        self.assertNotEqual(siguiente_binario_balanceado(4),7) 

    def test_anterior_binario_balanceado(self):
        self.assertEqual(anterior_binario_balanceado(3),2) 
        self.assertEqual(anterior_binario_balanceado(11),10)  
        self.assertTrue(anterior_binario_balanceado(3),2)  
        self.assertTrue(anterior_binario_balanceado(11),10)  
        self.assertNotEqual(anterior_binario_balanceado(11),12)  
        self.assertNotEqual(anterior_binario_balanceado(11),9)
  
    def test_binario_balanceado_mas_cercano(self):
        self.assertEqual(binario_balanceado_mas_cercano(3),2) 
        self.assertEqual(binario_balanceado_mas_cercano(11),12)  
        self.assertTrue(binario_balanceado_mas_cercano(11),12)  
        self.assertTrue(binario_balanceado_mas_cercano(3),2)  
        self.assertNotEqual(binario_balanceado_mas_cercano(3),1)  
        self.assertNotEqual(binario_balanceado_mas_cercano(6),7)  

unittest.main()
