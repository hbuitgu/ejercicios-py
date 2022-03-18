#4.	Juan tiene N cantidad de pesos, Camila tiene la mitad 
# de lo que posee Juan y Ricardo tiene la mitad de lo que
# poseen Camila y Juan Juntos. ¿Puede PYTHON ayudarme a calcular 
# la cantidad de dinero de los 3?


dineroJuan=int(input("Ingrese el dinero que tiene Juan"))
dineroCamila=dineroJuan/2
dineroRicardo=(dineroJuan+dineroCamila)/2
print("el dinero de camila es:",dineroCamila)
print("el dinero de ricardo es:",dineroRicardo)
print("el dinero de juan es:",dineroJuan)
