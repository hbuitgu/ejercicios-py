#23.	Leer 20 números enteros y guardar en una lista,
# después permitir que el usuario busque un número y si 
# este se encuentra en la lista indicar con un mensaje que
# el resultado es exitoso.

listaNumeros=[]

for i in range(0,20,1):
    numeroIngresado=int(input("Digite un numero:"))
    listaNumeros.append(numeroIngresado) # se agrega/crea el numero a la lista
buscarNumero= int(input("Ingrese numero a buscar:")) # buscarNumero es una varible y no una lsita por q esta en singular y no tiene []
if (buscarNumero in listaNumeros):
    print("Número encontrado en la lista")
else:
    print("Número no encontrado en la lista")