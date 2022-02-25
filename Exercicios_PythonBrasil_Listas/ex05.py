
def vetor_par_impar():
    print("\n---------------Exercício 05-----------------")
    vetor =[]
    par=[]
    impar =[]

    for numeros in range(20):
        num = int(input("\nInsira um numero inteiro: "))
        vetor.append(num)
        if num % 2 == 0:
            par.append(num)
        else:
            impar.append(num)
    print(f"Os números do vetor são {vetor}")
    print(f"Os números pares são {par}")
    print(f"Os números impares são {impar}")
vetor_par_impar()
