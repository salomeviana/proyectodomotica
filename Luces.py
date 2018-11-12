import serial  

#--------configuracion comunicacion python y arduino------------   

puerto=input("Ingrese el puerto Arduino:")
arduino = serial.Serial(puerto,9600)  
print (arduino.readline())   

#--------funciones para prender y apagar luces--------------            

def gard_ON():                                           
    arduino.write(b'1')   
    print("Las luces del jardin han sido encendidas")          
           
def gard_OFF():
    arduino.write(b'0') 
    print("Las luces del jardin han sido apagadas")
    
