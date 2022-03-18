#9.	Codificar un programa que presente un menú de 4 opciones
# y reciba un numero natural  para realizar las siguientes 
# operaciones:


import math
#variable controladora

#declaro el bucle/ciclo
#menu
print("Operación con números")
print("****")
print("0. para salir")
print("1. Digita 1 para indicar si el número es multiplo de 2#")
print("2. Digita 2 para calcular la raíz cuadrada de un número #")
print("3. Digita 3 para sumarle 100 al número ingresado")
print("4. Digita  para elevar al cuadrado el número ingresado ")
print("****")
opcion=1
while(opcion!=0):
    #variable controladora
    opcion=int(input("Digita una opcion:"))
    # pregunte por la opcion
    if(opcion==0):
        break
    elif(opcion==1):
        numero=int(input("Digita un numero:"))
        if numero%2==0 : 
            print("Es multiplo de 2")
        else:
            print("No es multiplo de 2")
    elif(opcion==2):
         numero=int(input("Digita un numero:"))
         raiz=math.sqrt(numero)
         print(f"La raiz de {numero} es{raiz}")
    elif(opcion==3):
        numero=int(input("Digita un nuemro:"))
        numerototal=numero+100
        print(f"El número es: {numero}, el total es: {numerototal}")
    elif(opcion==4):
        numero=int(input("Digita un numero:"))  
        potencia= math.pow(numero,2)
        print(f"El cuadrado de {numero} es: {potencia}")
    else: 
        print(f"Digite una opcion valida")