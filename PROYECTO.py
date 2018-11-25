from tkinter import *
"""Permite la creación de la interfaz gráfica"""
from tkinter import font
from FUNCIONES import *
#----ventana----------------------------

raiz=Tk() #Construir ventana que tiene como constructor Tk()
raiz.title("     M   Y     H   O   U   S   E")#Ponerle un titulo a la ventana
icono=raiz.iconbitmap("casita.ico")#Agrerar un icono a la ventana
raiz.geometry("1366x700")#Darle un tamaño determinado a la ventana

miImagen=PhotoImage(file="PLANTILLA.png")#Poner imagen de fondo a la ventana
Imagen=Label(image=miImagen,cursor="circle").place(x=0,y=0)#Hacer que mientras que el mouse esté sobre el fondo tenga un tipo de cursor establecido

#-----clave-------------------------------------

def verificacion_clave():
    """Verifica si la contrasena ingresada en el Entry de la ventana es correcta o no"""
    _clave=password.get()
    """Obtiene el texto ingresado en el cuadro Entry"""
    if _clave == "micasa":
        verify.config(text="HABILITADO",fg="green")
        """Modifica parametros del Label"""
        alarm_act.config(state=NORMAL)
        alarm_deact.config(state=NORMAL)
        """Modifica el estado de los Botones"""
        print("El sistema de alarmas ha sido habilitado")
    else:
        verify.config(text="INCORRECTA",fg="red")
        """Modifica parametros del Label"""
        print("se ha detectado un intento fallido de acceder al sistema")
        alarm_act.config(state=DISABLED)
        alarm_deact.config(state=DISABLED)
        """Modifica el estado de los Botones"""

#----caracteristicas de los botones----------------------------

on="ON"
off="OFF"
open="OPEN"
close="CLOSE"
one="1"
two="2"
three="3"
f_color="white"#color de fondo
l_color="black"#color de la letra
fc_color="black"#color de fondo de los botones al ser pulsados
lc_color="white"#color de la letra cuando los botones son pulsados
fuente= font.Font(family="Futurist Fixed-width", size=8)#tipo de fuente
typ_c="dot"#tipo de cursor cuando el mouse está sobre los botones, label o entry

#----creacion botones luces----------------------------

dr_on=Button(text=on,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color,command=droom_ON)
"""Se crea un objeto tipo Button y se le asignan parametros"""
dr_on.place(x=65,y=203)
"""Se posiciona el botón en la ventana a través de coordenadas del primer cuadrante del plano cartesiano"""

dr_off= Button(text=off,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color,command=droom_OFF)
dr_off.place(x=125,y=203)

automatic=Button(text="A ",bg="#bfbbb7",fg=l_color, font="arial 6", cursor=typ_c, activebackground=fc_color,activeforeground=lc_color,command=auto)
automatic.place(x=185,y=169)

manual=Button(text="M",bg="#bfbbb7",fg=l_color, font="arial 6", cursor=typ_c, activebackground=fc_color,activeforeground=lc_color,command=manu)
manual.place(x=205,y=169)


kit_park_on=Button(text=on,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color,command=kit_park_ON)
kit_park_on.place(x=65,y=330)

kit_park_off= Button(text=off,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color,command=kit_park_OFF)
kit_park_off.place(x=125,y=330)

 
tv_on=Button(text=on,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color,command=tvroom_ON)
tv_on.place(x=275,y=203)

tv_off= Button(text=off,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color,command=tvroom_OFF)
tv_off.place(x=335,y=203)


bed_rest_on=Button(text=on,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color,command=b_r_room_ON)
bed_rest_on.place(x=275,y=330)

bed_rest_off= Button(text=off,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color,command=b_r_room_OFF)
bed_rest_off.place(x=335,y=330)
 
 
gar_on=Button(text=on,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color, command=gard_ON)
gar_on.place(x=505,y=170)

gar_off= Button(text=off,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color, command=gard_OFF)
gar_off.place(x=565,y=170)

#----creacion botones puertas----------------------------
 
fd_open=Button(text=open,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color,command=fdoor_OPEN)
fd_open.place(x=65,y=470)

fd_close= Button(text=close,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color,command=fdoor_CLOSE)
fd_close.place(x=140,y=470)
 
 
pd_open=Button(text=open,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color,command=pdoor_OPEN)
pd_open.place(x=365,y=470)

pd_close= Button(text=close,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color,command=pdoor_CLOSE)
pd_close.place(x=440,y=470)
 
automaticpark=Button(text="A ",bg="#bfbbb7",fg=l_color, font="arial 6", cursor=typ_c, activebackground=fc_color,activeforeground=lc_color,command=autopark)
automaticpark.place(x=540,y=435)

manualpark=Button(text="M",bg="#bfbbb7",fg=l_color, font="arial 6", cursor=typ_c, activebackground=fc_color,activeforeground=lc_color,command=manu)
manualpark.place(x=560,y=435)

#----creacion botones elevador----------------------------
 
iniL_1=Button(text=one,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color,command=inilevel_1)
iniL_1.place(x=125,y=605)

iniL_2= Button(text=two,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color,command=inilevel_2)
iniL_2.place(x=125,y=635)

iniL_3= Button(text=three,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color,command=inilevel_3)
iniL_3.place(x=125,y=665)
 
 
finL_1=Button(text=one,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color,command=finlevel_1)
finL_1.place(x=405,y=605)

finL_2= Button(text=two,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color,command=finlevel_2)
finL_2.place(x=405,y=635)

finL_3= Button(text=three,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color,command=finlevel_3)
finL_3.place(x=405,y=665)

#----creacion botones alarma----------------------------

alarm_act=Button(text=" ACTIVATE ",bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color,state=DISABLED,command=activate)
alarm_act.place(x=880,y=350)

alarm_deact= Button(text="DEACTIVATE",bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color,state=DISABLED, command=deactivate)
alarm_deact.place(x=1100,y=350)


password=Entry(raiz)
"""Se crea un objeto tipo Entry"""
password.place(x=982,y=255)
"""Se posiciona el boton en la ventana a través de coordenadas del primer cuadrante del plano cartesiano"""
password.config(show="*", bg=f_color, fg=l_color, font=fuente, cursor=typ_c, selectbackground="black",width=10, justify="center",textvariable="")
"""Se le asignan parametros al Entry"""

pw_check=Button(text="✔",bg=f_color,fg=l_color, font="arial 7", cursor=typ_c, activebackground=fc_color,activeforeground=lc_color,command=verificacion_clave)
pw_check.place(x=1105,y=255)


verify=Label(raiz)
"""Se crea un objeto tipo Label"""
verify.place(x=983,y=285)
"""Se posiciona el Label en la ventana a través de coordenadas del primer cuadrante del plano cartesiano"""
verify.config(bg=f_color, font=fuente, cursor=typ_c,width=10, justify="center",text="")
"""Se le asignan parametros al Label"""


#----creacion botones ventilacion----------------------------

vent_on=Button(text=" ACTIVATE ",bg=f_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color,command=vent_ON)
vent_on.place(x=905,y=590)

vent_off= Button(text="DEACTIVATE",bg=f_color, font=fuente,cursor=typ_c, activebackground=fc_color,activeforeground=lc_color,command=vent_OFF)
vent_off.place(x=1075,y=590)


raiz.mainloop()#permite que se abra la ventana
