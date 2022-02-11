
def convert_fahr_for_celcius():
    print("\n------------------Execício 09------------------\n")

    dados = float(input("\n Insira o valor em graus Fahrenheit:  "))
    fahr_convertido =  5 * ((dados-32) / 9)
   
    print(f"\n O valor em Celsius é {fahr_convertido:,.2f}° ")
