can=0
cont=0
cont2=0
v=0
print("Cuanto dinero desea sacar?")
can=int(input())
if can>=1000:
    cont=can//1000
    v=can%1000
    if v>=200:
        cont2=v//200
        vu=v%200
        print(cont2)
    print(cont,"Tu dinero son ",cont," billetes de $1000. Y son ",cont2," billetes de $200. no hay billetes que cubran $",vu)
    