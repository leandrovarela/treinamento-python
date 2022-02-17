def big_num():
   print("\n---------------Exercício 06-----------------")
   
   num = []
   for numero in range (3):
      num.append(int(input(f"\nInsira o {1+numero}º valor: ")))
   
   
   maior= max(num)
   
   print(f"\n O maior numero inserido é {maior}")

big_num()


