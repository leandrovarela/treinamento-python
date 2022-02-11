'''
No exercicio1 tem uma funcao "elemento_esta_na_lista". Essa funcao recebe dois
parametros: um numero e uma lista de numeros. A funcao deve retornar True se 
o numero informado esta na lista. Caso contrario, deve retornar False.


No exercicio2 tem uma funcao "nome_esta_na_lista". Essa funcao recebe dois parametros:
uma string (nome) e uma lista de dicionarios, que deve ter a mesma estrutura da lista a seguir

lista = [
    {
        "nome": "Rogerio",
        "telefone": "132456789"
    },
    {
        "nome": "Fulano",
        "telefone": "102456789"
    },
    {
        "nome": "Beltrano",
        "telefone": "232456789"
    },
]

A função deve iterar sobre a lista e retornar o dicionario que contem o atributo "nome"
igual à string fornecida como parâmetro. Caso não haja esse elemento na lista, a função
deverá retornar None. Por exemplo, ao chamar a função passando "Rogerio" e a lista acima como parametro:

nome_esta_na_lista("Rogerio", lista), a mesma devera retornar:

{
    "nome": "Rogerio",
    "telefone": "132456789"
}

Atenção: Você deve editar apenas os arquivos exercicio1.py e exercicio2.py! Não se preocupe
com o arquivo valida_exercicios.py :)

Bons estudos!

'''

import valida_exercicios

valida_exercicios.valida_exercicio1()
valida_exercicios.valida_exercicio2()