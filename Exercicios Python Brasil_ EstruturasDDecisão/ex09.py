def orden_numbers():
    print("\n---------------Exercício 09-----------------")
    
    num = []
   
    num_01=int(input("\nInsira um valor: "))
    num.append(num_01)
    num_02=int(input("\nInsira um segundo valor: "))
    num.append(num_02)
    num_03=int(input("\nInsira um teceiro valor: "))
    num.append(num_03)

    ordem_crescente= sorted(num)
    
    print(f"\n Os numeros inserido em ordem crescente é {ordem_crescente}")

