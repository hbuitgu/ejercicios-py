#6.	Calcular la estación según un mes proporcionado por consola: 
# la estación del año

mesaño = input("Digita el mes del año:")
if (mesaño == "noviembre" or mesaño == "diciembre" or mesaño =="enero"):
    print(" Estamos en Invierno, abrigate")
elif (mesaño == "febrero" or mesaño == "marzo" or mesaño == "abril"):
    print("Estamos en Primavera, las flores florecen")
elif (mesaño == "mayo" or mesaño == "junio" or mesaño == "julio"):
    print(" Estamos en Verano, aplicate anti-solar")
elif (mesaño=="agosto" or mesaño == "septiembre" or mesaño == "octubre"):
    print("Estamis en  Otoño, a saltasr en las hojas")

else:
     print(" verifique, Mes no existe")
