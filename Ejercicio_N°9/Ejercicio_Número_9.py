iva=0
imp=0
f=0
print("De cuanto dinero es su importe?")
imp=int(input())
print("a su importe se le agregara un 21% de impuestos de IVA")
print(" ")
iva=(imp*21)/100
print("A su importe($",imp,") se le agregaron: $",iva,"de impuestos.")
f=imp+iva
print("Por lo tanto su importe final es de: $",f)