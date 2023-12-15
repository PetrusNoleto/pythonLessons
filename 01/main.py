listaDeNumeros = []

for i in range(2000, 10001):
    if (i%3==0) and (i%5==0) and (i%7==0) and (i%2!=0)and (i%8!=0): 
        listaDeNumeros.append(str(i))   

print(','.join(listaDeNumeros))        
