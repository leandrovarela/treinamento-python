def print_big_number():
    print("\n-------------------Exercício 11--------------------\n")    

    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))

    for num_1 in range(n1 + 1, n2):
        print(num_1)

    for num_2 in range(n2 + 1, n1):
        print(num_2)

    print("Soma dos números: ", num_1 + num_2)
print_big_number()