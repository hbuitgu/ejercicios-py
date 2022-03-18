#12.	Construir un programa que reciba números enteros y los sume mientras estos sean
# positivos, si se digita un número negativo el programa debe terminar.

sumaNumeros=0
numero=int(input("Ingrese un Numero positivo: "))

while numero >= 0:
        sumaNumeros=sumaNumeros+numero # se almacena numero ingresado
        numero=int(input("Ingrese un Numero:"))
    
print ("total:", sumaNumeros)      