


vogais=["a,e,i,o,u"]
quantVogais= 0
frase = input('Digite a frase: ')
branco = 0
for indice in frase:
    print(indice)
    if indice == " ":
        branco += 1
    if indice in "aeiou":
        quantVogais += 1

print('Total de espaços em branco: %d' % branco)
print('Total de vogais: %d' % quantVogais)
