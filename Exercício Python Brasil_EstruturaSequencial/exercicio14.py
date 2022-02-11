def joao_forrest_gump():
    print("\n------------------Execício 14------------------\n")

    pesoMaximo = 50
    peso = float(input("Digite a quantidade de kgs de peixe que João trouxe: "))
    if peso > pesoMaximo:
        excesso = peso - pesoMaximo
        multa = excesso * 4.00
        print (f"Multa foi de  {multa} reais")
        