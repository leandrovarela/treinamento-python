def date_validation():
    
    print("\n---------------Exercício 18-----------------")

    data = input("\nDigite uma data no formato dd/mm/aaaa: ")
    
    lista = data.split("/")
    valida = False
    
    dia=int(lista[0])
    mes= int(lista[1])
    ano= int(lista[2])

    if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
        
        if dia <= 31:
             valida = True
  
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        
        if dia <= 30:
            valida = True
             
    elif mes == 2:
       
        if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
            
            if dia <= 29:  
                valida = True
                
        elif dia <= 28:
            valida = True
    
    if(valida):
        
        print("Data válida\n")
        
    else:
        
        print("Inválida\n")
            
    