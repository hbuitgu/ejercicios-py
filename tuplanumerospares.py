#Convertir la tupla=(50,45,20,30,40,87) en una lista que solo contenga números  PARES

numerosTupla=(50,45,20,30,40,70)

listaNumeros=[] #lista vacia

for numeroTupla in numerosTupla:
    if numeroTupla%2==0:
        listaNumeros.append(numeroTupla)
    
print(listaNumeros)

## imprime los numeros pares del 20-70
print([i for i in range(20,71) if i%2==0]) #imprime los numeros pares en un rango detetminado


#Convertir la tupla=(50,45,20,30,40,87) en una lista que solo contenga números >40  
numerosTupla=(50,45,20,30,40,70)

listaNumeros=[] #lista vacia

for numeroTupla in numerosTupla:
    if numeroTupla>40:
        listaNumeros.append(numeroTupla) # append se envia el numero ingresado a la lista  
    
print(listaNumeros)

