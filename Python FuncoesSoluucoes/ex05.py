def somaImposta(taxaImposto, custo): 
    
    calculo = custo*taxaImposto/100
    soma = custo + calculo
    
    return print(soma)

somaImposta(5, 3000)