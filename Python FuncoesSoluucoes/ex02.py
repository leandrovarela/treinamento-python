def enes_dois(n):

    for row in range(1, n + 1):
        sequences = ""
        for col in range(1, row + 1):
            sequences += f"{col} "
        print(sequences)
        
   

