def sum_elements_square():
    print("\n---------------Exercício 09-----------------")
    vetorA= []
    resultados=[]
    for numeros in range(10):    
        vetorA.append(int(input(f"Insira o {numeros+1}º numero inteiro: ")))
            
    for numero in vetorA:
            
        resultados.append(numero**2)

    final=sum(resultados)
    print(f"O resultado da soma dos Quadrados dos elementos é {final}")

sum_elements_square()
