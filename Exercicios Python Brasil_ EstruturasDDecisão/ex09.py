def orden_numbers():
    print("\n---------------Exercício 09-----------------")
    
    num = []
    for number in range(3):
        num.append(int(input("\nInsira um valor: ")))
        

    ordem_crescente= sorted(num)
    
    print(f"\n Os numeros inserido em ordem crescente é {ordem_crescente}")

