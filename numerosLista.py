#Construir un programa que reciba el tamaño de una lista y
# la llene con números entregados por el usuario.

numerosLista=[]

tamano=int(input("Ingrese el tamaño de la lista:"))

for i in range(tamano):
    numero=int(input("Ingrese el número de la lista:"))
    numerosLista.append(numero)
print(numerosLista)    


