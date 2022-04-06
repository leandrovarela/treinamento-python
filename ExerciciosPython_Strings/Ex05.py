def print_vertical(name):
    
   for indice in range(len(name)):
        print(indice ,name[:len(name)-indice].upper())
# Iteração de for começa de indice 0 .
# no programa a cima temos um for  com range do inicio da iteração até o tamanho dela inteira.
# após definimos no print que o intervalo é o len(name)"Tamanho inteiro da Variável" - a iteração dela.
#dando um efeito de escada reversa.
#importante ressaltar que entender qual indice está iterando é mega importante para resolução do problema. 
print_vertical("paralelepipedo")