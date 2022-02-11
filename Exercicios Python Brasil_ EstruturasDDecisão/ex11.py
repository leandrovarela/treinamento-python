def payment_pl():
   print("\n---------------Exercício 11-----------------")

   salario = float(input("\nDigite o seu salário: R$"))

   salario_baixo = salario * 0.20
   final_sal_baixo = salario * 1.20

   salario_medio = salario * 0.15
   final_sal_medio = salario * 1.15

   salario_alto = salario * 0.10
   final_sal_alto = salario * 1.10

   salario_altissimo = salario * 0.05
   final_sal_alti = salario * 1.05

   print("Antes Reajuste: ", salario)

   if salario <= 280: 

      print("Aumento: 20%\nValor: ", salario_baixo, "\nFinal: ",final_sal_baixo)

   elif salario > 200 and salario <= 700: 

      print("Aumento: 15%\nValor: ", salario_medio, "\nFinal: ", final_sal_medio)

   elif salario > 700 and salario <= 1500: 

      print("Aumento: 10%\nValor: ", salario_alto, "\nFinal: ", final_sal_alto)

   else:
       print("Aumento: 5%\nValor: ", salario_altissimo, "\nFinal: ", final_sal_alti)

