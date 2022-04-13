
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
        mostrar = self.cor
        return mostrar
print(Bola.mostra_cor("Amarelo"))