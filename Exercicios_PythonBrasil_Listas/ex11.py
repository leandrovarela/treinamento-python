import random

def listas_intercaladas_plus():
    print("\n---------------Exercício 11-----------------")
    lista1 = []
    lista2 = []
    lista3 = []
    lista4 = []

    for index in range(10):
        lista1.append(random.randint(1,100))
        lista2.append(random.randint(1,100))
        lista3.append(random.randint(1,100))
    
        lista4.append(lista1[index])
        lista4.append(lista2[index])
        lista4.append(lista3[index])

    print(lista1)
    print(lista2)
    print(lista3)
    print(lista4)


   