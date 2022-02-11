def point_average_abc():
   
   print("\n---------------Exercício 14-----------------")


   nota_1=float(input("\nInsira a primeira nota do aluno: "))
   nota_2=float(input("\nInsira a segunda nota do aluno: "))
   media= float(nota_1+nota_2)/2


   if media >= 9 and media < 10:

      print(f"\nPrimeira nota :{nota_1}\nSegunda nota :{nota_2}\nA média do aluno:{media}\Conceito: A\n APROVADO")

   elif media > 7.5 :

      print(f"\nPrimeira nota :{nota_1}\nSegunda nota :{nota_2}\nA média do aluno:{media}\nConceito: B\nAPROVADO")

   elif media >= 6 :

      print(f"\nPrimeira nota :{nota_1}\nSegunda nota :{nota_2}\nA média do aluno:{media}\nConceito: C\nAPROVADO")

   elif media == 4 and media <6: 
      print(f"\nPrimeira nota :{nota_1}\nSegunda nota :{nota_2}\nA média do aluno:{media}\nConceito: D\nREPROVADO")
   else:
     
     print(f"\nPrimeira nota :{nota_1}\nSegunda nota :{nota_2}\nA média do aluno:{media}\nConceito: E\nREPROVADO")


