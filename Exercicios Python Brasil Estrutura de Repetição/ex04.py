def population():
        print("\n-------------------Exercício 04--------------------\n")
        a = 80000
        b = 300000 
        ano = 0
        tax_a = 0.03
        tax_b = 0.015
        
        while a <= b:
            a += a * tax_a
            b += b * tax_b        
            ano += 1
    
        print (f"\nA população de (A) ultrapassa ou iguala ao país (B) em {ano} anos")
            

