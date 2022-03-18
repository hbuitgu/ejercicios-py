
#3.	Recibir dos números y determinar cual es mayor

numero1 = int(input("Ingrese el primer número: ")) #Preguntamos al usuario qué número quiere
numero2= int(input("Ingrese es el segundo número: "))
if numero1>numero2:
   print(numero1,'es mayor que', numero2)
elif numero1<numero2:
  print(numero1,'es menor que',numero2)
else:
  print(numero1,'Es igual a', numero2)
