"""

def enquete():
    print("\n---------------Exercício 19-----------------")
    votos=[]
    voto_plus=[]
    print("\nQual o melhor Sistema Operacional para uso em servidores?\n\nAs possíveis respostas são:\n1- Windows Server\n2- Unix\n3- Linux\n4- Netware\n5- Mac OS\n6- Outro")
    voto = int(input("Insira um numero de 1 a 6 e 0 para finalizar: "))
    while True:
        if voto >= 1 and voto <=6:
            votos.append(voto)
            voto = int(input("Insira um numero de 1 a 6 e 0 para finalizar: ")) 
        elif voto == 0:
            windows=votos.count(1)
            voto_plus.append(windows)

            unix=votos.count(2)
            voto_plus.append(unix)

            linux=votos.count(3)
            voto_plus.append(linux)

            netware=votos.count(4)
            voto_plus.append(netware)

            mac_os=votos.count(5)
            voto_plus.append(mac_os)

            outro=votos.count(6)
            voto_plus.append(outro)

            total= unix+linux+windows+netware+mac_os+outro
            print("----------------------------------------------")
            print(f"Sistema Operacional    Votos    %")
            print("---------------------  ------   ----")
            print(f"Windows Sever           {windows}       {(windows/total)*100:,.2f}")
            print(f"Unix                    {unix}       {(unix/total)*100:,.2f}")
            print(f"Linux                   {linux}       {(linux/total)*100:,.2f}")
            print(f"Netware                 {netware}       {(netware/total)*100:,.2f}")
            print(f"Mac_Os                  {mac_os}       {(mac_os/total)*100:,.2f}")
            print(f"Outro                   {outro}       {(outro/total)*100:,.2f}")
            print("---------------------  ------   ----")
            print(f"Total de Votos:         {total}")
            
            if max(voto_plus) == 1:
                print(f" O vencedor é Windows com {windows} e com a porcentagem de {(windows/total)*100:,.2f}%")
            elif max(voto_plus) == 2:
                print(f" O vencedor é Unix com {unix} e com a porcentagem de {(unix/total)*100:,.2f}%")
            elif max(voto_plus) == 3:
                print(f" O vencedor é Linux com {linux} e com a porcentagem de {(linux/total)*100:,.2f}%")  
            elif max(voto_plus) == 4:
                print(f" O vencedor é Netware com {netware} e com a porcentagem de {(netware/total)*100:,.2f}%")  
            elif max(voto_plus) == 5:
                print(f" O vencedor é Mac_Os com {mac_os} e com a porcentagem de {(mac_os/total)*100:,.2f}%")  
            elif max(voto_plus) == 6:
                print(f" O vencedor é Outro com {outro} e com a porcentagem de {(outro/total)*100:,.2f}%")          
            break
        else:
            print("Valor inválido")
    
            voto = int(input("Insira um numero de 1 a 6 e 0 para finalizar: "))
    
    
enquete()
"""
from enum import Enum, auto

class SOEnum(Enum):
    WINDOWS = 1
    UNIX = auto()
    LINUX = auto()
    NETWARE= auto()
    MAC = auto()
    OUTROS = auto()
    

nome_por_id = {
    SOEnum.WINDOWS.value: 'Windows',
    SOEnum.UNIX.value: 'Unix',
    SOEnum.LINUX.value: 'Linux',
    SOEnum.NETWARE.value: 'Netware',
    SOEnum.MAC.value: 'Mac',
    SOEnum.OUTROS.value: 'Outros',
}
    

votos_por_sistema = {
    SOEnum.WINDOWS.value: 0,
    SOEnum.UNIX.value: 0,
    SOEnum.LINUX.value: 0,
    SOEnum.NETWARE.value: 0,
    SOEnum.MAC.value: 0,
    SOEnum.OUTROS.value: 0,
}

inputSistema = int(input("Digite o sistema que recebera um voto: "))
votos_por_sistema[inputSistema] += int(input("Digite o voto: "))


def ehMaiorVoto(nome_so):
    return votos_por_sistema.get(nome_so) == max(votos_por_sistema.values())
    
mais_votados = filter(ehMaiorVoto, votos_por_sistema.keys())

print(f"Os mais votados foram {[f'SO: {nome_por_id[so]}; Votos:{votos_por_sistema[so]}' for so in mais_votados]}")

