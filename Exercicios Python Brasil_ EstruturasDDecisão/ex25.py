def detetive():
  print("\n---------------Exercício 25-----------------")

  resp =[]
  print("\nResponda apenas com sim ou não: ")

  a=str(input("\nsTelefonou para a vítima? ").lower())
  resp.append(a)

  b=str(input("Esteve no local do crime? ").lower())
  resp.append(b)

  c=str(input("Mora perto da vítima? ").lower())
  resp.append(c)
  
  d=str(input("Devia para a vítima? ").lower())
  resp.append(d)

  e=str(input("Já trabalhou com a vítima? ").lower())
  resp.append(e)

  pontos = resp.count("sim")

  print(f"\nvocê fez {pontos} pontos")

  if pontos == 2:

    print("\nClassificado como: Suspeito")

  if pontos == 3 or pontos == 4:

    print("\nClassificado como: Cúmplice")

  if pontos == 5:

    print("\nClassificado como: Assassino")

  elif pontos == 0 or pontos == 1:

    print("\nClassificado como: Inocente")

