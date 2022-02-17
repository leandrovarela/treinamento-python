from datetime import date

def date_validation():
    print("\n---------------Exercício 18-----------------")
    
    data = input("\nDigite uma data no formato dd/mm/aaaa: ")
    
    try:
        dia, mes, ano = [int(item) for item in data.split("/")]
        date(ano, mes, dia)
        print("Data válida")
    
    except Exception as error:
        print("Data incorreta!")


