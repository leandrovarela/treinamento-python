import random 
def mult_dados():
    print("\n---------------Exercício 24-----------------")
    dados=[]
    for dado in range (1,101):
        dados.append(random.randint(1,6))
    face_um=dados.count(1)
    face_dois=dados.count(2)
    face_tres=dados.count(3)
    face_quatro=dados.count(4)
    face_cinco=dados.count(5)
    face_seis= dados.count(6)
    print(f"Os resultados dos dados foram: \n\n Número 01 : {face_um} vezes\n Número 02 : {face_dois} vezes\n Número 03 : {face_tres} vezes \n Número 04 : {face_quatro} vezes\n Número 05 : {face_cinco} vezes\n Número 06 : {face_seis} vezes")
mult_dados()