
class Bola:
    def __init__(self, cor: str, circuferencia: str, material: str):
        self.cor= cor
        self.circuferencia =circuferencia
        self.material= material
    #def __repr__(self) -> str:
    #    return 
    
    def troca_cor(self, new_cor: str):
        self.cor = new_cor
        return new_cor

    def mostra_cor(self):
        return self.cor

b= Bola("Amarelo","33mm","Couro")      
b2= Bola("Verde","34mm","Borracha")      
b3= Bola("Cinza","35mm","Couro Sintético")

print(b.mostra_cor())
print(b2.mostra_cor())
print(b3.mostra_cor())
print(b.troca_cor("Vermelho"))
print(b.mostra_cor())
