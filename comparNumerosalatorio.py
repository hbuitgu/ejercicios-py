import random
x=random.randint(0, 5)
y=random.randint(0, 5)
print(x)
print(y)
if x>y:
 print(x,'es mayor que',y)
elif x<y:
 print(x,'es menor que',y)
else:
 print(x,'es igual a',y)