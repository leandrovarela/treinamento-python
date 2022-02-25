def age_height():
   print("\n---------------Exercício 08-----------------")
   altura=[]
   idade= []
   for pessoa in range (1, 6):
      idade.append(int(input(f"\nDigite a idade da pessoa {pessoa}: ")))
      altura.append(float(input(f"Digite sua altura da pessoa {pessoa}: ")))
   
   idade.reverse()
   altura.reverse() 
   print(f" \nA lista dos dados das pessoas invertida:  Idade {idade}, altura {altura}")

age_height()
