#1.	Una compañía de software contable, paga a su 
# personal de ventas un salario de 3500000 mensuales, 
# mas una comisión de 1500000 por cada licencia de software 
# vendida menos el (5% del salario total + comisiones de deducciones) 
# por impuestos. Codifica un programa que calcule e imprima el salario 
# mensual de un vendedor dado recibiendo el numero de ventas realizadas


licencia = int(input("Ingrese la cantidad de Lincencias de sotware vendidas:"))
salario=3500000
comision  = 1500000*licencia
impuesto = comision*0.05
salarioTotal= salario+comision-impuesto
print("Su salario es:",salarioTotal)