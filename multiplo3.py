#recibir un numero por teclado y determinar si es multiplo de 3

Num = int(input("Ingrese un numero:"))
 
if Num%3==0 : #el porcentaje es el que me arroja el residuo de la dividion 
    print("Es multiplo de 3")
else:
    print("No es multiplo de 3")