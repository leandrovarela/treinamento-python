def print_big_number():
    print("---------------Exercício 01-----------------")

    x = int(input("\nInsira um numero: "))
    y = int(input("\nInsira outro numero: "))

    if (x > y) :
        print(f"\nO numero {x} é maior que {y}")
    elif (x == y):
        print("\nOs numeros inseridos são iguais ")   
    else: 
        print(f"\nO numero {y} é maior que {x}")