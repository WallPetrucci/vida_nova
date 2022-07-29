from Calculadora import Calculadora

class TestCalculadora:
    def setup_class(self):
        self.calculadora = Calculadora()
        
    def test_somar(self):
        assert self.calculadora.somar(3, 3) == 6
        assert self.calculadora.somar("2", "2") == 4
        assert self.calculadora.somar("2A", "E") == "Não vale entrada de letras"
    
    def test_subtrair(self):
        assert self.calculadora.subtrair(3, 3) == 0
        assert self.calculadora.subtrair("12", "10") == 2
        assert self.calculadora.subtrair("2A", "E") == "Não vale entrada de letras"
    
    def test_multiplicar(self):
        assert self.calculadora.multiplicar(3, 3) == 9
        assert self.calculadora.multiplicar("5", "10") == 50
        assert self.calculadora.multiplicar("2A", "E") == "Não vale entrada de letras"
    
    def test_dividir(self):
        assert self.calculadora.dividir(3, 3) == 1
        assert self.calculadora.dividir("10", "5") == 2
        assert self.calculadora.dividir("2A", "E") == "Não vale entrada de letras"