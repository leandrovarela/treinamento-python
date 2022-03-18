
valorFatura=float(input("Insira o valor da fatura:R$ "))
diasAtraso=int(input("Digite agora os dias em atraso:"))


def valorPagamento(valorFatura,diasAtraso):
        if diasAtraso == 0:
            total= valorFatura  
        else:
            total= (valorFatura*0.03)+((valorFatura*0.001)*diasAtraso)+valorFatura


        return total

print(f"O relatório é: \n {valorPagamento(valorFatura,diasAtraso)}")


