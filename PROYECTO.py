from tkinter import *
from tkinter import font
from Luces import *
#----ventana----------------------------

raiz=Tk() #construir ventana que tiene como constructor Tk()
raiz.title("     M   Y     H   O   U   S   E")
icono=raiz.iconbitmap("casita.ico")
raiz.geometry("1366x700")
vp=Frame()

miImagen=PhotoImage(file="PLANTILLA.png")
Imagen=Label(image=miImagen,cursor="circle").place(x=0,y=0)

#-----clave-------------------------------------
clave=""

def verificacion_clave():
    _clave=password.get()
    if _clave == "micasa":
        verify.config(text="HABILITADO",fg="green")
        alarm_act.config(state=NORMAL)
        alarm_deact.config(state=NORMAL)
        print("El sistema de alarmas ha sido habilitado")
    else:
        verify.config(text="INCORRECTA",fg="red")
        print("se ha detectado un intento fallido de acceder al sistema")


#----caracteristicas de los botones----------------------------

on="ON"
off="OFF"
open="OPEN"
close="CLOSE"
one="1"
two="2"
three="3"
f_color="white"
l_color="black"
fc_color="black"
lc_color="white"
fuente= font.Font(family="Futurist Fixed-width", size=8)
typ_c="dot"

#----creacion botones luces----------------------------

dr_on=Button(text=on,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color,command=droom_ON)
dr_on.place(x=65,y=203)

dr_off= Button(text=off,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color,command=droom_OFF)
dr_off.place(x=125,y=203)


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

alarm_deact= Button(text="DEACTIVATE",bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color,state=DISABLED)
alarm_deact.place(x=1100,y=350)


password=Entry(raiz)
password.place(x=982,y=255)
password.config(show="*", bg=f_color, fg=l_color, font=fuente, cursor=typ_c, selectbackground="black",width=10, justify="center",textvariable=clave)

pw_check=Button(text="✔",bg=f_color,fg=l_color, font="arial 7", cursor=typ_c, activebackground=fc_color,activeforeground=lc_color,command=verificacion_clave)
pw_check.place(x=1105,y=255)


verify=Label(raiz)
verify.place(x=983,y=285)
verify.config(bg=f_color, font=fuente, cursor=typ_c,width=10, justify="center",text="")


#----creacion botones ventilacion----------------------------

vent_on=Button(text=" ACTIVATE ",bg=f_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color,command=vent_ON)
vent_on.place(x=905,y=590)

vent_off= Button(text="DEACTIVATE",bg=f_color, font=fuente,cursor=typ_c, activebackground=fc_color,activeforeground=lc_color,command=vent_OFF)
vent_off.place(x=1075,y=590)






raiz.mainloop()
