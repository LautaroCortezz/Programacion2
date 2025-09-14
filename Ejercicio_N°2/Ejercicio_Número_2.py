intento=0
import random
numero=random.randint(1.,20)
for x in range (1,7,1):
     while (numero!=intento):
        print("intente adivinar el numero random que tengo,es del 1 al 20.")
        intento=int(input())
        if intento==numero:
            print(intento," es el numero que tengo,felecidades.")
        else:
           if intento>numero:
               print(intento," Mi numero es menor. Intentelo de nuevo.")
           else:
               print(intento,"Mi número es mayor.Intentelo de nuevo.")