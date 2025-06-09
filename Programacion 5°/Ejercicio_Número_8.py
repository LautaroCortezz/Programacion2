import math
a=0
p=0
p2=0
r=0
v=0
al=0
pu=0
uni=""
opc=""
print("Hola, ¿Quiere sacar el area del círculo o el volumen de un cilindro?")
print("Si quiere sacar el area del círculo coloque a o A, pero si quiere sacar el Volumen de un cilindro coleque v o V")
opc=input()
if opc=="a" or opc=="A":
    print("¿me podria decir que radio tiene el círculo?")
    p=int(input())
    a=math.pi*(p**2)
    pu=a//1
    print("¿me podria decir en que unidad esta el circulo?")
    uni=input()
    print("su area es de ",pu,uni,"cuadrados, aproximadamente")
    
else:
    print("¿me podria decir que radio tiene el cilindro?")
    p=int(input())
    a=math.pi*(p**2)
    print("¿me podria decir cual es la altura del cilindro(solo números)?")
    al=int(input())
    v=a*al
    pu=v//1
    print("¿me podria decir en que unidad esta el cilindro")
    uni=input()
    print("su volumen es de",pu,uni,"cubicos, aproximadamente")