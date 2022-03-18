#Etapas de la vida 0-14 niño
#15-28 joven
#28- 60 adulto
#>60 adulto mayor
edad=int(input("Digite la Edad:"))
if (edad==0 or edad<=14):
    print("Es un niño")
elif (edad==15 or edad<=28):
    print("joven")
elif (edad==29 or edad<=60):
    print("Adulto")
else:
    print("Adulto Mayor")

