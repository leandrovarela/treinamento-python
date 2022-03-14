def converterData(hora):
    convert=hora -12 
    return convert

def imprime_hora(hora,minuto):
    print("-------------Exercício 06-------------")
    if(hora <= 12):
        resultado=print(f"{hora}:{minuto} AM ")
    else:
        resultado=print(f"{converterData(hora)}:{minuto} PM ")
    return resultado

    
