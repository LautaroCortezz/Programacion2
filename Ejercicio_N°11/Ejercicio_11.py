import random
listaE=["Lautaro","Joaquin","Benja","Theo","Jere","Tomas","Santino"]
numero=random.sample(range(1,8),7)
for a in range(0,7):
    print("El alumno",listaE[a],"va a pasar a exponer ",numero[a],"°")