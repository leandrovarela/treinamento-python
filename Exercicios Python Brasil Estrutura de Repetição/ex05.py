def insert_population():
    print("\n-------------------Exercício 05--------------------\n")
    cont = 0
    ano = 0
    a = int(input("\nInsira os números de habitantes do País A:  "))
    b = int(input("\nInsira os números de habitantes do País B:  "))
    tax_a = float(input("\nAgora insira a taxa de crescimento do país A: "))
    tax_b = float(input("\nAgora insira a taxa de crescimento do país B: "))
    while a <= b:
        a += a * tax_a
        b += b * tax_b        
        ano += 1      
        print (f"\nA população de (A) ultrapassa ou iguala ao país (B) em {ano} ano(s)")
        cont= input("\nQuer continuar (S/N) ?")   
        if cont == "S" or cont == "s": 
            a = int(input("\nInsira os números de habitantes do País A:  "))
            b = int(input("\nInsira os números de habitantes do País B:  "))
            tax_a = float(input("\nAgora insira a taxa de crescimento do país A: "))
            tax_b = float(input("\nAgora insira a taxa de crescimento do país B: "))
            print (f"\nA população de (A) ultrapassa ou iguala ao país (B) em {ano} ano(s)")
        else: 
            print("fim do programa")
            break

