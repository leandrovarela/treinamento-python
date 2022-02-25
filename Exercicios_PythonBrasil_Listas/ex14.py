def investigation():
   print("\n---------------Exercício 14-----------------")
   perguntas=["Telefonou para a vítima?","Esteve no local do crime?","Mora perto da vítima?","Devia para a vítima?","Já trabalhou com a vítima?"]
   quantidade=[]

   for resposta in perguntas:
      print(resposta)
      quantidade.append(str(input("Responda sim ou não: ")))
      pontos= quantidade.count("sim")
      print(quantidade)
      print(pontos)

   if pontos == 2:
         print("\nSuspeito")
   elif pontos == 3 or pontos == 4:
         print("\nCumplice")
   elif pontos == 5:
         print("\nAssasino")
   else:
         print("\nInocente")

