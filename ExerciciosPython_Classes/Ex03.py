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
        print(f"As medidas do Retângulo são:")
        return self.comprimento,self.largura

    def calcula_area(self):
        area= self.comprimento * self.largura
        return area

    def calcula_perimetro(self):
        perimetro= 2*(self.largura + self.comprimento)
        return perimetro


x =float(input("Insira o comprimento: "))
y =float(input("Insira a largura: "))

a = Retangulo(x,y)
print(a.mostra_medidas())
print(a.calcula_perimetro())
print(a.calcula_area())
print(a.altera_comprimento(9))
print(a.altera_largura(10))
print(a.mostra_medidas())
print(a.calcula_perimetro())
print(a.calcula_area())

print (f"serão necessários {a.calcula_area()}m² quadrado(s) de piso e {a.calcula_perimetro()}m de rodapés para suprir o local")

 