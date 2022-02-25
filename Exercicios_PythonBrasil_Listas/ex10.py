import random

def listas_intercaladas():
    print("\n---------------Exercício 10-----------------")
    lista1 = []
    lista2 = []
    lista3 = []


    for index in range(10):
        lista1.append(random.randint(1,100))
        lista2.append(random.randint(1,100))
        
        lista3.append(lista1[index])
        lista3.append(lista2[index])
       
    print(lista1)
    print(lista2)
    print(lista3)
