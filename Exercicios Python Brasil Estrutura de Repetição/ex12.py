def tabuada():
    print("\n-------------------Exercício 12--------------------\n")

    tabuada=int(input("Tabuada do numero: "))

    for count in range(11):
        result= tabuada *count
        print(f"{tabuada} x {count} = {result}")
