import serial  
"""Permite la comunicacion con Arduino atraves del puerto serie"""

#--------CONFIGURACION COMUNICACION PYTHON Y ARDUINO------------   

puerto=input("Ingrese el puerto Arduino:")#Pide que el usuario ingrese el puerto por el que se va a realizar la comunicacion serial y lo guarda en la variable puerto.
arduino = serial.Serial(puerto,9600)  #Se crea el objeto arduino atraves de la clase Serial y se abre la comunicacion con el puerto serie con el puerto ingresado por el usuario a una velocidad de transmision 9600 baudios
print (arduino.readline())
"""Imprime la informacion enviada por Arduino"""

#--------LUCES--------------         
 
def droom_ON():
    """Prender luz comedor
    Envia a Arduino el caracter 'g' atraves del puerto serial que permite encender la luz del comedor
    Imprime un mensaje en la consola"""   
    arduino.write('g'.encode())
    print("The dining-room lights have been turned on.")
     
def droom_OFF():
    """Apagar luz comedor
    Envia a Arduino el caracter 'h' atraves del puerto serial que permite apagar la luz del comedor
    Imprime un mensaje en la consola"""   
    arduino.write('h'.encode())
    print("The dining-room lights have been turned off.")
     
def auto():
    """Modo automatico
    Envia a Arduino el caracter 'y' atraves del puerto serial que permite poner el bombillo del comedor en modo automatico 
    Imprime un mensaje en la consola"""   
    arduino.write('y'.encode())
    print("Automatic mode activated.")
     
def manu():
    """Modo manual
    Envia a Arduino el caracter 'Z' atraves del puerto serial que permite poner el bombillo del comedor y la puerta del parqueadro en modo manual
    Imprime un mensaje en la consola"""   
    arduino.write('Z'.encode())
    print("Manual mode activated.")
     
def kit_park_ON():
    """Prender luces cocina y parqueadero
    Envia a Arduino el caracter 'i' atraves del puerto serial que permite encender las luces de la cocina y parqueadero
    Imprime un mensaje en la consola"""   
    arduino.write('i'.encode())   
    print("The parking and kitchen lights have been turned on.")
      
def kit_park_OFF():
    """Apagar luces cocina y parqueadero
    Envia a Arduino el caracter 'j' atraves del puerto serial que permite apagar las luces de la cocina y parqueadero
    Imprime un mensaje en la consola"""   
    arduino.write('j'.encode())   
    print("The parking and kitchen lights have been turned off.")
         
def tvroom_ON():
    """Prender luces sala de television
    Envia a Arduino el caracter 'k' atraves del puerto serial que permite encender las luces de la sala de television
    Imprime un mensaje en la consola"""   
    arduino.write('k'.encode())   
    print("The tv-room lights have been turned on.")
          
def tvroom_OFF():
    """Apagar luces sala de television
    Envia a Arduino el caracter 'l' atraves del puerto serial que permite apagar las luces de la sala de television
    Imprime un mensaje en la consola"""   
    arduino.write('l'.encode())   
    print("The tv-room lights have been turned off.")  
        
def b_r_room_ON():
    """Apagar luces de cuarto y bano
    Envia a Arduino el caracter 'm' atraves del puerto serial que permite apagar las luces del cuarto y bano
    Imprime un mensaje en la consola"""
    arduino.write('m'.encode())   
    print("The bedroom and restroom lights have been turned on.")    
      
def b_r_room_OFF():
    """Apagar luces cuarto y bano
    Envia a Arduino el caracter 'n' atraves del puerto serial que permite apagar las luces de la sala del cuarto y bano
    Imprime un mensaje en la consola"""   
    arduino.write('n'.encode())   
    print("The bedroom and restroom lights have been turned off.")  
           
def gard_ON():
    """Prender luces jardin
    Envia a Arduino el caracter 'o' atraves del puerto serial que permite encender las luces del jardin
    Imprime un mensaje en la consola"""                                             
    arduino.write('o'.encode())   
    print("The garden lights have been turned on.")          
             
def gard_OFF():
    """Apagar luces jardin
    Envia a Arduino el caracter 'p' atraves del puerto serial que permite apagar las luces del jardin
    Imprime un mensaje en la consola""" 
    arduino.write('p'.encode()) 
    print("The garden lights have been turned off.")
      
#--------------------------PUERTAS---------------------------
def fdoor_OPEN():
    """Abrir puerta principal
    Envia a Arduino el caracter 'q' atraves del puerto serial que permite abrir la puerta principal
    Imprime un mensaje en la consola"""   
    arduino.write('q'.encode())
    print("Front door open.")
      
def fdoor_CLOSE():
    """Cerrar puerta principal
    Envia a Arduino el caracter 'r' atraves del puerto serial que permite cerrar la puerta principal
    Imprime un mensaje en la consola"""   
    arduino.write('r'.encode())
    print("Front door closed.")
      
def pdoor_OPEN():
    """Abrir puerta parqueadero
    Envia a Arduino el caracter 's' atraves del puerto serial que permite cerrar la puerta del parqueadero
    Imprime un mensaje en la consola"""   
    arduino.write('s'.encode())
    print("Parking door open.")
      
def pdoor_CLOSE():
    """Cerrar puerta parqueadero
    Envia a Arduino el caracter 't' atraves del puerto serial que permite cerrar la puerta del parqueadero
    Imprime un mensaje en la consola"""    
    arduino.write('t'.encode())
    print("Parking door closed.")
     
def autopark():
    """Modo automatico
    Envia a Arduino el caracter 'z' atraves del puerto serial que permite poner la puerta del parqueadero en modo automatico
    Imprime un mensaje en la consola"""   
    arduino.write('z'.encode())
    print("Automatic mode activated.")
#-------------------------ELEVADOR---------------------------
#---------pedir------------------------------------------
def inilevel_1():
    """Pedir piso 1
    Envia a Arduino el caracter 'a' atraves del puerto serialque permite pedir el ascensor al primer piso"""   
    arduino.write('a'.encode())
     
def inilevel_2():
    """Pedir piso 2
    Envia a Arduino el caracter 'b' atraves del puerto serialque permite pedir el ascensor al segundo piso"""
    arduino.write('b'.encode())
     
def inilevel_3():
    """Pedir piso 3
    Envia a Arduino el caracter 'c' atraves del puerto serialque permite pedir el ascensor al tercer piso"""
    arduino.write('c'.encode())
     
#---------mandar------------------------------------------
     
def finlevel_1():
    """Mandar piso 1
    Envia a Arduino el caracter 'd' atraves del puerto serialque permite mandar el ascensor al primer piso""" 
    arduino.write('d'.encode())
     
def finlevel_2():
    """Mandar piso 2
    Envia a Arduino el caracter 'e' atraves del puerto serialque permite mandar el ascensor al segundo piso""" 
    arduino.write('e'.encode())
     
def finlevel_3():
    """Mandar piso 3
    Envia a Arduino el caracter 'f' atraves del puerto serialque permite mandar el ascensor al tercer piso""" 
    arduino.write('f'.encode())
     
#-------------------------ALARMAS----------------------------
def activate():
    """Activar alarma
    Envia a Arduino el caracter 'u' atraves del puerto serial que permite activar el sistema de alarmas
    Imprime un mensaje en la consola"""
    arduino.write('u'.encode())
    print("The alarm system has been activated.")
     
def deactivate():
    """desactivar alarma
    Envia a Arduino el caracter 'v' atraves del puerto serial que permite desactivar el sistema de alarmas
    Imprime un mensaje en la consola"""
    arduino.write('v'.encode())
    print("The alarm system has been deactivated")
#-------------------------VENTILACION-----------------------
  
def vent_ON():
    """Activar ventilacion
    Envia a Arduino el caracter 'w' atraves del puerto serial que permite activar el sistema de ventilacion
    Imprime un mensaje en la consola"""                                          
    arduino.write('w'.encode())   
    print("Ventilation system activated.")          
             
def vent_OFF():
    """desactivar ventilacion
    Envia a Arduino el caracter 'x' atraves del puerto serial que permite desactivar el sistema de ventilacion
    Imprime un mensaje en la consola"""
    arduino.write('x'.encode()) 
    print("Ventilation system deactivated.")