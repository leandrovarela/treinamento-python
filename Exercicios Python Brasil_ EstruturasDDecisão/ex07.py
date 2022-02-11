def big_num_and_small():
   print("\n---------------Exercício 07-----------------")
   
   num = []
   # x, y,z são os respectivos números a serem adicionados na lista
   x=int(input("\nInsira um valor: "))
   num.append(x)
   y=int(input("\nInsira um segundo valor: "))
   num.append(y)
   z=int(input("\nInsira um teceiro valor: "))
   num.append(z)

   maior= max(num)
   menor= min(num)
   
   print(f"\n O maior numero inserido é {maior} e o menor é {menor}")