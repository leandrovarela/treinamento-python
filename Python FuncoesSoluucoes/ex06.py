def converterData(hora):

    return (hora-12)

def imprime_hora(hora,minuto):
    if(hora <= 12):
        resultado=print(f"{hora}:{minuto} AM ")
    else:
        resultado=print(f"{converterData(hora)}:{minuto} PM ")
    return resultado

    
imprime_hora(13,56)