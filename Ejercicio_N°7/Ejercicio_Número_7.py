#esto lo uso para que el programa muestre el mes en español
import locale

locale.setlocale(locale.LC_TIME,"es_ES.UTF-8")

#Aca llamamos a la funcion datetime
from datetime import datetime

fecha_nac=input("ingrese su fecha de nacimiento (Formato:DD/MM/AAAA): ")

#Para convertir se fecha en formato: estructura de tiempo=
fecha_estructura=datetime.strptime(fecha_nac,"%d/%m/%Y")

#colocamos el día de hoy
dia=datetime.now()

#sacamos la diferencia
diferencia=dia -fecha_estructura
print("Su edad en días es de ",diferencia.days," días desde tu nacimiento")

#llamamos a la funcion time
import time

#Para convertir se fecha en formato: estructura de tiempo PERO en el formato time=
fecha_est=time.strptime(fecha_nac,"%d/%m/%Y")
fecha_leg=time.strftime("%d de %B de %Y",fecha_est)
print("Su fecha de nacimiento es : ",fecha_leg)