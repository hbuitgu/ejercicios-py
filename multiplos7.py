# 16.	Construir un programa que reciba el tamaño de una lista
# y la llene con múltiplos de 7
multiplos=[1]
longitudLista=int(input("ingresar el tramaño de la lista"))

for i in range(longitudLista):
    multiplos.append(i+1*7) #append agrega elementos a la lista(caja)
print(multiplos)