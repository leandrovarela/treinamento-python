def triangule():
    print("\n---------------Exercício 15----------------")

    a = float(input("\nPrimeiro lado: "))
    b = float(input("\nSegundo  lado: "))
    c = float(input("\nTerceiro lado: "))

    
    if (a + b < c) or (a + c < b) or (b + c < a):

        print("\nNão é um triângulo")
        
    elif (a == b) and (a == c) :

        print("\nEquilátero")
    elif (a==b) or (a==c) or (b==c):

        print("\nIsósceles")
    else:
        print("\nEscaleno")

