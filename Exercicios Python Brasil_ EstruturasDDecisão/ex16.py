import math
def delta():
   print("\n---------------Exercício 16-----------------")
    
   print("\nEquaçao do 2° grau da forma: ax² + bx + c")
    
   a = int( input("\nCoeficiente a: ") )

   if(a==0):
        print(" Não é equação do segundo grau")
   else:
      b = int( input("\nCoeficiente b: ") )
      c = int( input("\nCoeficiente c: ") )

      delta = b*b - (4*a*c)

      if delta < 0:

            print("\nDelta negativo a equação não possui Raízes reais")

      elif delta==0:
         raiz = -b / (2*a)

         print(f"\nEquação possui 1 Raiz= {raiz}")

      else:
         raiz1 = (-b + math.sqrt(delta) ) / (2*a)
         raiz2 = (-b - math.sqrt(delta) ) / (2*a)

         print(f"\nEquação possuí 2 Raizes:{raiz1} e {raiz2}")

