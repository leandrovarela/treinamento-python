def converterData(hora, minuto):
    hour = hora - 12 
    min = minuto
    indicador = ""
    return
    
def parse(hora, minuto, indicador):
    indicador= "PM" if hora > 12 else "AM"
    print(f"{hora}:{minuto} {indicador}")

converterData(19, 45)