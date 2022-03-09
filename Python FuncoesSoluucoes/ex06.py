def converterData(hora, minuto, indicador):
    hour = hora - 12 
    min = minuto
    indicador= "PM" if hora > 12 
     else: "AM"

def parse( hora , minuto):