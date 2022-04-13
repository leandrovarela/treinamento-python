class Quadrado:
    def __init__(self, lado: float):
        self.lado= lado
    
    def altera_lado(self, new_lado: float):
        self.lado = new_lado
        return new_lado

    def mostra_lado(self):
        return self.lado
    
    def calcula_area(self):
        area= self.lado * self.lado
        return area

q=Quadrado(7)
print(q.mostra_lado())
print(q.calcula_area())
print(q.altera_lado(8))
print(q.calcula_area())