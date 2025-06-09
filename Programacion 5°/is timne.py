import time

#print(time.ctime(0))

#print(time.time())

#print(time.ctime(time.time()))

#tiempoact=time.localtime()
#print(tiempoact)

#tiempo_actual=time.localtime()
#tiempo=time.strftime("%B %d %y %H:%M:%S ", tiempo_actual)
#print(tiempo)

cadenaDeTiempo="21 October, 2008"
tiempo=time.strptime(cadenaDeTiempo, "%d %B, %Y")
#print(tiempo)

tiempotupla=(2025,4,14,4,20,0,0,0,0)
cadena_tiempo=time.asctime(tiempotupla)
print(cadena_tiempo)

tiempotupla=(2025,4,14,4,20,0,0,0,0)
cadena_tiempo=time.mktime(tiempotupla)
print(cadena_tiempo)