#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *

ventana=Tk()
ventana.title('CALCULADORA')
ventana.geometry('362x640')
ventana.configure(backgroun='SkyBlue4')
color_boton=('gray77')

ancho_boton=11
alto_boton=3
input_text=StringVar()
operador=''

Salida=Entry(ventana,font=('arial',20,'bold'),width=22,textvariable=input_text,bd=20,insertwidth=4,bg='powder blue',justify='right')
Salida.place(x=10,y=60)

Button(ventana,text='√',bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(0)).place(x=17,y=180)
Button(ventana,text='π',bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(0)).place(x=107,y=180)
Button(ventana,text='^',bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(0)).place(x=197,y=180)
Button(ventana,text='!',bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(0)).place(x=287,y=180)

Button(ventana,text='AC',bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(0)).place(x=17,y=240)
Button(ventana,text='( )',bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(0)).place(x=107,y=240)
Button(ventana,text='%',bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(0)).place(x=197,y=240)
Button(ventana,text='/',bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(0)).place(x=287,y=240)

Button(ventana,text='7',bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(0)).place(x=17,y=300)
Button(ventana,text='8',bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(0)).place(x=107,y=300)
Button(ventana,text='9',bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(0)).place(x=197,y=300)
Button(ventana,text='+',bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(0)).place(x=287,y=300)

Button(ventana,text='4',bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(0)).place(x=17,y=360)
Button(ventana,text='5',bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(0)).place(x=107,y=360)
Button(ventana,text='6',bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(0)).place(x=197,y=360)
Button(ventana,text='-',bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(0)).place(x=287,y=360)

Button(ventana,text='1',bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(0)).place(x=17,y=420)
Button(ventana,text='2',bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(0)).place(x=107,y=420)
Button(ventana,text='3',bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(0)).place(x=197,y=420)
Button(ventana,text='+',bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(0)).place(x=287,y=420)

Button(ventana,text=',',bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(0)).place(x=17,y=480)
Button(ventana,text='0',bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(0)).place(x=107,y=480)
Button(ventana,text='eliminar',bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(0)).place(x=197,y=480)
Button(ventana,text='=',bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(0)).place(x=287,y=480)










