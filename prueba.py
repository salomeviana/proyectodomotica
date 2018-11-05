from tkinter import *
from tkinter import font

#----ventana----------------------------

raiz=Tk()#construir ventana que tiene como constructor Tk()
raiz.title("     M   Y     H   O   U   S   E")
icono=raiz.iconbitmap("casita.ico")
raiz.geometry("1366x700")
vp=Frame()

miImagen=PhotoImage(file="PLANTILLA.png")
Imagen=Label(image=miImagen,cursor="circle").place(x=0,y=0)

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

dr_on=Button(text=on,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color)
dr_on.place(x=65,y=200)
dr_off= Button(text=off,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color)
dr_off.place(x=125,y=200)

kit_on=Button(text=on,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color)
kit_on.place(x=65,y=270)
kit_off= Button(text=off,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color)
kit_off.place(x=125,y=270)

park_on=Button(text=on,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color)
park_on.place(x=65,y=340)
park_off= Button(text=off,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color)
park_off.place(x=125,y=340)
 
tv_on=Button(text=on,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color)
tv_on.place(x=275,y=200)
tv_off= Button(text=off,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color)
tv_off.place(x=335,y=200)

bed_on=Button(text=on,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color)
bed_on.place(x=275,y=270)
bed_off= Button(text=off,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color)
bed_off.place(x=335,y=270)
 
rest_on=Button(text=on,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color)
rest_on.place(x=275,y=340)
rest_off= Button(text=off,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color)
rest_off.place(x=335,y=340)
 
gar_on=Button(text=on,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color)
gar_on.place(x=505,y=170)
gar_off= Button(text=off,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color)
gar_off.place(x=565,y=170)

#----creacion botones puertas----------------------------
 
fd_open=Button(text=open,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color)
fd_open.place(x=65,y=470)
fd_close= Button(text=close,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color)
fd_close.place(x=140,y=470)
 
pd_open=Button(text=open,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color)
pd_open.place(x=365,y=470)
pd_close= Button(text=close,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color)
pd_close.place(x=440,y=470)
 
 #----creacion botones elevador----------------------------
 
iniL_1=Button(text=one,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color)
iniL_1.place(x=125,y=605)
iniL_2= Button(text=two,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color)
iniL_2.place(x=125,y=635)
iniL_3= Button(text=three,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color)
iniL_3.place(x=125,y=665)
 
finL_1=Button(text=one,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color)
finL_1.place(x=405,y=605)
finL_2= Button(text=two,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color)
finL_2.place(x=405,y=635)
finL_3= Button(text=three,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color)
finL_3.place(x=405,y=665)

 #----creacion botones alarma----------------------------

alarm_act=Button(text=" ACTIVATE ",bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color)
alarm_act.place(x=880,y=350)
alarm_deact= Button(text="DEACTIVATE",bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color)
alarm_deact.place(x=1100,y=350)

password=Entry(raiz)
password.place(x=982,y=255)
password.config(show="*",bg=f_color, fg=l_color, font=fuente, cursor=typ_c, selectbackground="black",width=10, justify="center")
pw_check=Button(text="✔",bg=f_color,fg=l_color, font="arial 7", cursor=typ_c, activebackground=fc_color,activeforeground=lc_color)
pw_check.place(x=1105,y=255)

 #----creacion botones ventilacion----------------------------

vent_on=Button(text=on,bg=f_color,fg=l_color, font=fuente, cursor=typ_c, activebackground=fc_color,activeforeground=lc_color)
vent_on.place(x=1120,y=570)
vent_off= Button(text=off,bg=f_color,fg=l_color, font=fuente,cursor=typ_c, activebackground=fc_color,activeforeground=lc_color)
vent_off.place(x=1180,y=570)




    



raiz.mainloop()