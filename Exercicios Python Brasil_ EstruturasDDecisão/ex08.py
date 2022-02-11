def small_price():
   print("\n---------------Exercício 08-----------------")
   
   p1 = float(input("\nDigite o preço 1° produto/ Preço: R$ "))
   p2 = float(input("\nDigite o preço 2° produto /Preço: R$ "))
   p3 = float(input("\nDigite o preço 3° produto/ Preço: R$ "))

   if p1 < p2 and p3 > p1:

      print(f"\nO produto 1 de R${p1} é o mais barato e a melhor escolha!")

   elif p2 < p1 and p3 > p2:

      print (f"\nO produto 2 de R${p2} é o mais barato e a melhor escolha!")

   elif p3 < p1 and p2 > p3:
      print(f"\nO produto 3 de R${p3} é o mais barato e a melhor escolha!")

    #Se alguns numeros forem iguais
   elif p1 == p2 and p1 and p2 < p3:
      print(f"O produto 1 de {p1} e 2 {p2} tem o mesmo preço e são os mais baratos!")
   elif (p1 == p3) and p1 and p3 < p2:
      print(f"O produto 1 de{p1}  e 3 {p3} tem o mesmo preço e são os mais baratos!")
   elif p2 == p3 and p2 and p3 < p1:
      print(f"O produto 1 de {p1} e 2 {p2} tem o mesmo preço e são os mais baratos!")

    #Se todo os numero forem iguais

   else:
      print('Todos os preços são iguais!!')
