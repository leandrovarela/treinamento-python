def print_imp_par():
    par= []
    impar =[]
    for numeros in range(10):
        num_temp = int(input("Insira um numero inteiro: "))
        if(num_temp % 2) == 0:
            par.append(num_temp)
        else:
            impar.append(num_temp)

    print(f"Numeros pares ({len(par)}) e numeros pares({len(impar)})")
print_imp_par()