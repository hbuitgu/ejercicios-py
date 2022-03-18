#Leer 8 ciudades colombianas, guardarlas en una lista 
# y mostrar en orden inverso los datos ingresados

# inversed invierte el orde de la lista

ciudades=["medellin", "cali", "bogota","pereira", "santa marta", "cartagena", "barranquilla", "manizales"]
print(ciudades)

for ciudad in reversed(ciudades):
    print(ciudad)


# otra forma con len que me da la longitud de la lista
ciudades = ["medellin", "cali", "bogota","pereira", "santa marta", "cartagena", "barranquilla", "manizales"]
print(ciudades)
listaciudades = len(ciudades)
for i in range(listaciudades):
      print(ciudades[listaciudades-i-1])