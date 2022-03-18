
valorFatura=float(input("Insira o valor da fatura:R$ "))
diasAtraso=int(input("Digite agora os dias em atraso:"))
total=""

def valorPagamento(valorFatura,diasAtraso,total):
    if diasAtraso >= 0:
        total= valorFatura  
    else:
        total= (valorFatura*0.03)+(diasAtraso*0.001)

    
    return print(f"Você pagará {total}")



