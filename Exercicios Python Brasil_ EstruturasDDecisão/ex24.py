def obtem_informacoes_numero(num):
    paridade = 'par' if num%2 == 0 else 'ímpar'
    sinal = None
    if num > 0:
        sinal = 'positivo'
    elif num < 0:
        sinal = 'negativo'
    else:
        sinal = 'neutro'
    tipo = 'inteiro' if num%1 == 0 else 'decimal'
    return f"{num} é {paridade}, {sinal}, {tipo}"
def mult_types():
    print("\n---------------Exercício 24-----------------")
    numero_01= float(input("\nInsira um número:"))
    numero_02= float(input("\nInsira outro número: "))
    operacao = str(input("Digite a operação (M - nultiplicar, D- divisão)"))
    if operacao.lower() == "m":
        resultado = numero_01*numero_02
        print(f"{resultado} é: {obtem_informacoes_numero(resultado)}")
mult_types()