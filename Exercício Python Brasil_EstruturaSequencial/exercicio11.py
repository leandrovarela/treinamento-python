
def calculate_double_int_one_real():
    print("\n------------------Execício 11------------------\n")
    
    num_1= int(input("Insira um valor inteiro: "))
    num_2= int(input("Insira um segundo valor inteiro: "))
    num_real= float(input("Insira um numero real:  "))

    a= (num_1*2)*(num_2/2)
    b=(num_1*3)+ num_real
    c= num_real**3
    print("\n A. O produto do dobro do primeiro com metade do segundo ")
    print(f"R: {a}")

    print("\n B. A soma do triplo do primeiro com o terceiro ")
    print(f"R: {b:,.2f}")

    print("\n C. O terceiro elevado ao cubo ")
    print(f"R: {c:,.2f}")