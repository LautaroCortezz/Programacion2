bacterias=1
sas=0
print("Cuantas horas quieres esperar?")
sas=int(input())
for x in range (1,sas+1,1):
    print("en ",x," horas hay ",bacterias," bacterias")
    bacterias=bacterias*2