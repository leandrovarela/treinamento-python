class Retangulo:
    def __init__(self, comprimento: float, largura: float ):
        self.comprimento= comprimento
        self.largura = largura

    def altera_comprimento(self, new_comprimento: float):
        self.comprimento = new_comprimento
        return new_comprimento
        
    def altera_largura(self,new_largura: float):
        self.largura= new_largura
        return new_largura

    def mostra_medidas(self):
        return f"As medidas do Retângulo são: Comprimento {self.comprimento}cm,Largura {self.largura}cm."

    def calcula_area(self):
        area= self.comprimento * self.largura
        return area

    def calcula_perimetro(self):
        perimetro= 2*(self.largura + self.comprimento)
        return perimetro
    def informa_gastos(self):
        return f"Serão necessários {self.calcula_area()}m² quadrado(s) de piso e {self.calcula_perimetro()}m de rodapés para suprir o local."
        

x =float(input("Insira o comprimento: "))
y =float(input("Insira a largura: "))

a = Retangulo(x,y)
print(a.informa_gastos())

 