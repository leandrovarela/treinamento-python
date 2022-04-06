def triangule():
    print("\n---------------Exercício 15----------------")
    lista=[]
    num= 0

    while num != -1:
        num= int(input("Insira um valor: "))
        lista.append(num)
       
    
    print(len(lista))
    print(lista)
    ele=lista.reverse()
    for elemento in ele:
        
        print(elemento)

