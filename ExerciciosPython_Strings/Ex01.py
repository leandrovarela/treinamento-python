def compara_strings(*strings):
    print("Compara duas strings:")

    for indice in range(len(strings)) :

        print("String" , indice+1, ":", strings[indice])
    for indice in range(len(strings)):

        print(" Tamanho de :",strings[indice],":" ,len(strings[indice]), "caracteres")
    
    if len(strings[0]) == len(strings[1]):
        print("As duas strings são de tamanhos iguais.")
    else:
        print("As duas strings são de tamanhos diferentes")

    if strings[0] == strings[1]:
        print("As duas strings possuem conteúdo iguais")

    else:
        print("As duas strings possuem conteúdo diferentes")

compara_strings("Estou treinando com Camila","Estou treinando com Camila")
