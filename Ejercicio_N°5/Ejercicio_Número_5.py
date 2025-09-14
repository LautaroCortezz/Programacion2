r=0
c=0
es=0
print("cuantos caramelos se van a repartir")
c=int(input())
print("Cuantos estudiantes son?")
es=int(input())
r=c//es
s=c%es
print(r," caramelos para cada estudiante")
print("le sobran ",s," caramelos.")