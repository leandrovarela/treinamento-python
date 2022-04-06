from math import prod

def sum_mult_print():

    print("\n---------------Exercício 07-----------------")
    num= []
    for numero in range(5):
        num.append(int(input(f"\nInsira o {numero+1}º número: ")))
    
    soma= sum(num)
    multi= prod(num)
    
    print(f" A soma dos elementos é : {soma}  e a Multiplicação é : {multi} ")
    print(f"E os numeros foram {num}")
    

   