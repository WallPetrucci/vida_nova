class Calculadora:
    def somar(self, num1, num2):
        try:
            return int(num1) + int(num2)
        except ValueError:
            return "Não vale entrada de letras"
    
    def subtrair(self, num1, num2):
        try:
            return int(num1) - int(num2)
        except ValueError:
            return "Não vale entrada de letras"
    
    def dividir(self, num1, num2):
        try:
            return int(num1) / int(num2)
        except ValueError:
            return "Não vale entrada de letras"
    
    def multiplicar(self, num1, num2):
        try:
            return int(num1) * int(num2)
        except ValueError:
            return "Não vale entrada de letras"