numeros=[[1,2,3,4],
         [5,6,7,8],
         [9,10,11,12],
         [13,14,15,16]]
cont=4
suma=0
multi2=1
cont2=-1
suma2=0
multi=1
for j in range(0,4):
    cont2=cont2+1
    suma=numeros[j][cont2]+suma
    multi=numeros[j][cont2]*multi
    cont=cont-1
    suma2=numeros[j][cont]+suma2
    multi2=numeros[j][cont]*multi2
    print(suma2)
    print(multi2)
    
print("la suma de la diagonal es: ", suma)
print("la multiplicacion de la diagonal principal es: ", multi)
print ("La suma de la contradiagonal es: ",suma2)
print("la multiplicacion de la diagonal principal es: ",multi2)
