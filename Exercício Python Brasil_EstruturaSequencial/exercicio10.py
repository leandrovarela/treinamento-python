def convert_celsius_for_fahr():
    print("\n------------------Execício 10------------------\n")

    dados = float(input("Insira o valor de Celsius para ser convertido:  "))
    celsius_convertido = dados * 1.80 + 32    
    
    print(f"\n O valor em Fahrenheit é {celsius_convertido:,.2f}° ")
