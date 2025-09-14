num=0
hexa=0
boe=0
opcion=""
entero=0
print("que numero queres pasar a Binario Y Hexadecimal ")
num=int(input())
print("Su número esta en Binario(B), Hexadecimal(H) o en Decimal(D)? ")
opcion=input()
if opcion=="B":
    entero=int(num)
    hexa=hex(num)
    print("Su numero en Decimal es: ",entero,". Y su numero en Hexadecimal es: ",hexa)
else:
    if opcion=="H":
        binario=bin(num)
        entero=int(num)
        print("Su numero en Decimal es: ",entero,". Y su numero en Binario es: ",binario)

    else:
        hexa=hex(num)
        binario=bin(num)
        print("Su numero en Binario es: ",binario,". Y su numero en Hexadecimal es: ",hexa)
