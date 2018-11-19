import serial  

#--------CONFIGURACION COMUNICACION PYTHON Y ARDUINO------------   

puerto=input("Ingrese el puerto Arduino:")
arduino = serial.Serial(puerto,9600)  
print (arduino.readline())   

#--------LUCES--------------            
 
def droom_ON():
    arduino.write('g'.encode())
    print("Las luces de la sala han sido encendidas")
     
def droom_OFF():
    arduino.write('h'.encode())
    print("Las luces de la sala han sido apagadas")
     
def kit_park_ON():
    arduino.write('i'.encode())   
    print("Las luces del jardin han sido encendidas")
     
def kit_park_OFF():
    arduino.write('j'.encode())   
    print("Las luces del jardin han sido encendidas")
        
def tvroom_ON():
    arduino.write('k'.encode())   
    print("Las luces del jardin han sido encendidas")
         
def tvroom_OFF():
    arduino.write('l'.encode())   
    print("Las luces del jardin han sido encendidas")  
       
def b_r_room_ON():
    arduino.write('m'.encode())   
    print("Las luces del jardin han sido encendidas")    
     
def b_r_room_OFF():
    arduino.write('n'.encode())   
    print("Las luces del jardin han sido encendidas")  
          
def gard_ON():                                           
    arduino.write('o'.encode())   
    print("Las luces del jardin han sido encendidas")          
            
def gard_OFF():
    arduino.write('p'.encode()) 
    print("Las luces del jardin han sido apagadas")
     
#--------------------------PUERTAS---------------------------
def fdoor_OPEN():
    arduino.write('q'.encode())
    print("puerta principal abierta")
     
def fdoor_CLOSE():
    arduino.write('r'.encode())
    print("puerta principal cerrada")
     
def pdoor_OPEN():
    arduino.write('s'.encode())
    print("puerta parqueadero abierta")
     
def pdoor_CLOSE():
    arduino.write('t'.encode())
    print("puerta parqueadero cerrada")
#-------------------------ELEVADOR---------------------------
#---------pedir------------------------------------------
def inilevel_1():
    arduino.write('a'.encode())
    
def inilevel_2():
    arduino.write('b'.encode())
    
def inilevel_3():
    arduino.write('c'.encode())
    
#---------mandar------------------------------------------
    
def finlevel_1():
    arduino.write('d'.encode())
    
def finlevel_2():
    arduino.write('e'.encode())
    
def finlevel_3():
    arduino.write('f'.encode())
#-------------------------ALARMAS----------------------------
def activate():
    arduino.write('u'.encode())
    
def deactivate():
    arduino.write('v'.encode())
#-------------------------VENTILACION-----------------------
 
def vent_ON():                                           
    arduino.write('w'.encode())   
    print("Sistema de ventilacion encendido")          
            
def vent_OFF():
    arduino.write('x'.encode()) 
    print("Sistema de ventilacion apagado")