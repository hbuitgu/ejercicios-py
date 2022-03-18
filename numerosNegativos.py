#Pedir 20 números y contar cuantos de los ingresados fueron negativos

i=1
sumanegativos=0
sumapositivos=0

while i <=5:
    numero=int(input(f"Ingresa el numero {i}:")) ## para q los mensajes se impriman numerados
    i+=1
    if numero < 0:
       sumanegativos=sumanegativos+1 
       
    else:
        sumapositivos+=1
            
print(f"{sumanegativos} numeros son negativos")       