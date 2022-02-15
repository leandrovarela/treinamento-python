def num_inter_int():
    print("\n-------------------Exercício 10--------------------\n")

    num1=int(input("digite um numero: "))
    num2=int(input("digite outro numero: "))
    while num2<num1:
        num1=int(input("digite um numero: "))
        num2=int(input("digite outro numero: "))
    else:
        for numb in range(num1,num2,1):
            print(numb)
            result=(sum(numb))
            print(result)

num_inter_int()