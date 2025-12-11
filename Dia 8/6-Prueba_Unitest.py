import unittest
import cambia_texto_Unittest


class ProbarCambiarTexto(unittest.TestCase):
    def test_mayuscula(self):
        palabra = 'buen dia'
        resultado = cambia_texto_Unittest.todo_mayuscula(palabra)
        self.assertEqual(resultado, 'BUEN DIA')


if __name__ == '__main__':
    unittest.main()
