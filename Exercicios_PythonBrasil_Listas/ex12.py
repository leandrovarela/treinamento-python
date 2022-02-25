def media_members():
    idades = [10, 15, 9, 12, 13, 12, 14,15,13,15,14,15,16,12,25,12,14,13,12,13,14,15,13,15
    ,13,14,15,15,12,14]

    alturas = [1.40, 1.35, 1.36, 1.38, 1.37, 1.46, 1.20, 1.40, 1.26, 1.27, 1.17, 1.35, 1.50, 1.36, 1.27, 1.37, 1.23, 1.24
    ,1.25, 1.24, 1.35, 1.34, 1.29, 1.34, 1.23, 1.25, 1.27, 1,36, 1.35]


    mediaAltura = sum(alturas)/len(alturas)
    quantidadeAlunos = 0

    for i in range(0, len(idades)):
        if idades[i] > 13 and alturas[i] < mediaAltura:
            quantidadeAlunos = quantidadeAlunos + 1

    print (f"{quantidadeAlunos} alunos possuem mais de 13 anos e altura inferior a  média de altura dos alunos")

