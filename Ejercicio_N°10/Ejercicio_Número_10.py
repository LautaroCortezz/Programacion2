x=0
def factorial(n):                 #con esto definimos el numero
    if n==0 or n==1:              #Con esto vemos si n es 0 o 1 y devolvemos 1,por que 0!=1! es decir 1 
        return 1                  #Hacemos que devuelva el 1
    return n*factorial (n-1)#Hacemos que devuelva el factorial(n) y colocamos que re le reste dentro del parentesis 1 y lo multiplicamos por el mismo número.
print("¿qué número quiere factorizar?")
x=int(input())
print(factorial(x))               #Mostramos el resultado de factorial
