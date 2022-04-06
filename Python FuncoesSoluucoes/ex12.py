import random
 
def embaralha(palavra):
    palavra = palavra.lower()

    embaralha = random.sample(palavra, len(palavra)) # String vira lista
    nova = ''.join(embaralha) # lista vira string
    
    return nova


    