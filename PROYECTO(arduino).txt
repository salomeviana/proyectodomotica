#include <Servo.h>
//------------------PUERTAS-----------------------------------------------
Servo puerta;
Servo parqueadero;
const int fotopark=A4;
int voltaje_fotopark;
int umbralpark=300;
//------------------ASCENSOR--------------------------------------------
int piso1=13;
int piso2=12;
int piso3=11;
int MA=10;
int MB=9;
//------------------BOMBILLO-----------------------------------------------
const int bombillo=8;
const int foto=A5;
int voltaje_foto=0;
int umbral=512;
//------------------LUCES-----------------------------------------------
const int kit_park=7;
const int tv=4;
const int b_r_room=3;
const int gard=2;
//------------------VENTILACION-----------------------------------------------
const int ventilador=A0;
//------------------ALARMA-----------------------------------------------
const int sensor= A1;
int buzzer =A2;
const int LEDPin=A3;
//------------LECTURA DESDE PYTHON-----------------------------------------------
char value=0;

void setup() 
   { 
      Serial.begin(9600);
//------------------ASCENSOR--------------------------------------------
      pinMode(piso1, INPUT);
      pinMode(piso2, INPUT);
      pinMode(piso3, INPUT);
      pinMode(MA, OUTPUT);
      pinMode(MB, OUTPUT);
//------------------BOMBILLO-----------------------------------------------
      pinMode(bombillo, OUTPUT);
//------------------LUCES----------------------------------------------- 
      pinMode(kit_park, OUTPUT);
      digitalWrite (kit_park, LOW);
      pinMode(tv, OUTPUT);
      digitalWrite (tv, LOW);
      pinMode(b_r_room, OUTPUT);
      digitalWrite (b_r_room, LOW);
      pinMode(gard, OUTPUT);
      digitalWrite (gard, LOW);
//------------------VENTILACION-----------------------------------------------
      pinMode(ventilador, OUTPUT);
//------------------ALARMA-----------------------------------------------
      pinMode(buzzer, OUTPUT);
      pinMode(LEDPin, OUTPUT);
      pinMode(sensor, INPUT);
//------------------PUERTAS-----------------------------------------------
      puerta.attach(6);
      puerta.write(90);
      parqueadero.attach(5);
      parqueadero.write(96);
//------------------CONEXION-----------------------------------------------
      Serial.println("Conectado...");
   }
 
void loop() 
   {
     while (Serial.available())
        {
           value = Serial.read();
        }
//////////////////////////////ASCENSOR//////////////////////////////

//------------------PISO 1--------------------------
 //-----------------pedir del 1 al 1------------------
if (digitalRead(piso1) == LOW && value == 'a' )
{
 digitalWrite(MA,LOW);
 digitalWrite(MB,LOW); 
}

 //-----------------pedir del 2 al 1------------------
if (digitalRead(piso2) == LOW && value == 'a' )
{
 while (digitalRead(piso1) == HIGH)
 {
 digitalWrite(MA,LOW);
 digitalWrite(MB,HIGH); 
 }
}

 //-----------------pedir del 3 al 1------------------
if (digitalRead(piso3) == LOW && value == 'a' )
{
 while (digitalRead(piso1) == HIGH)
 {
 digitalWrite(MA,LOW);
 digitalWrite(MB,HIGH); 
 }
}
//-----------------mandar a P1------------------
if (digitalRead(piso1) == LOW && value== 'd')
{
 digitalWrite(MA,LOW);
 digitalWrite(MB,LOW);
}

//-----------------mandar a P2------------------
if (digitalRead(piso1) == LOW && value == 'e')
{
  while (digitalRead(piso2) == HIGH)
  {
    digitalWrite(MA,HIGH);
    digitalWrite(MB,LOW); 
  }
}

//-----------------mandar a P3------------------
if (digitalRead(piso1) == LOW && value == 'f')
{
  while (digitalRead(piso3) == HIGH)
  {
    digitalWrite(MA,HIGH);
    digitalWrite(MB,LOW); 
  }
}

 //------------------PISO 2--------------------------
 //-----------------pedir del 1 al 2------------------
if (digitalRead(piso1) == LOW && value == 'b' )
{ while (digitalRead(piso2) == HIGH)
 {
 digitalWrite(MA,HIGH);
 digitalWrite(MB,LOW); 
 }
}

 //-----------------pedir del 2 al 2------------------
if (digitalRead(piso2) == LOW && value == 'b' )
{
 digitalWrite(MA,LOW);
 digitalWrite(MB,LOW); 
}

 //-----------------pedir del 3 al 2------------------
if (digitalRead(piso3) == LOW && value == 'b' )
{
 while (digitalRead(piso2) == HIGH)
 {
 digitalWrite(MA,LOW);
 digitalWrite(MB,HIGH); 
 }
}
//-----------------mandar a P1------------------
if (digitalRead(piso2) == LOW && value== 'd')
{
   while (digitalRead(piso1) == HIGH)
   {
    digitalWrite(MA,LOW);
    digitalWrite(MB,HIGH);
   }
}

//-----------------mandar a P2------------------
if (digitalRead(piso2) == LOW && value == 'e')
{
    digitalWrite(MA,LOW);
    digitalWrite(MB,LOW); 
}

//-----------------mandar a P3------------------
if (digitalRead(piso2) == LOW && value == 'f')
{
  while (digitalRead(piso3) == HIGH)
  {
    digitalWrite(MA,HIGH);
    digitalWrite(MB,LOW); 
  }
}
 //------------------PISO 3--------------------------
 //-----------------pedir del 1 al 3------------------
if (digitalRead(piso1) == LOW && value == 'c' )
{ while (digitalRead(piso3) == HIGH)
 {
 digitalWrite(MA,HIGH);
 digitalWrite(MB,LOW); 
 }
}

 //-----------------pedir del 2 al 3------------------
if (digitalRead(piso2) == LOW && value == 'c' )
{
   while (digitalRead(piso3) == HIGH)
 {
 digitalWrite(MA,HIGH);
 digitalWrite(MB,LOW); 
 }

}

 //-----------------pedir del 3 al 3------------------
if (digitalRead(piso3) == LOW && value == 'c' )
{
 digitalWrite(MA,LOW);
 digitalWrite(MB,LOW); 
}
//-----------------mandar a P1------------------
if (digitalRead(piso3) == LOW && value== 'd')
{
   while (digitalRead(piso1) == HIGH)
   {
    digitalWrite(MA,LOW);
    digitalWrite(MB,HIGH);
   }
}

//-----------------mandar a P2------------------
if (digitalRead(piso3) == LOW && value == 'e')
{  while (digitalRead(piso2) == HIGH)
  {
    digitalWrite(MA,LOW);
    digitalWrite(MB,HIGH); 
  }

}

//-----------------mandar a P3------------------
if (digitalRead(piso3) == LOW && value == 'f')
{
    digitalWrite(MA,LOW);
    digitalWrite(MB,LOW); 
}

//////////////////////////////BOMBILLO//////////////////////////////
    voltaje_foto = analogRead(foto);
    if (value == 'h')
      {
        digitalWrite(bombillo,LOW);
      } 

     else if (value == 'g')
      {
      digitalWrite(bombillo,HIGH);
      }

      else if (value== 'y' && voltaje_foto>=umbral)
      {
        digitalWrite(bombillo,HIGH);
      }
      else if (value== 'y' && voltaje_foto<umbral)
      {
        digitalWrite(bombillo,LOW);
      }
//////////////////////////////LUCES//////////////////////////////
     if (value == 'i')
     {
      digitalWrite (kit_park, HIGH);
     }
     else if (value == 'j')
     {
      digitalWrite (kit_park, LOW);
     }

     else if (value == 'k')
     {
      digitalWrite (tv, HIGH);
     }
     else if (value == 'l')
     {
      digitalWrite (tv, LOW);
     }

     else if (value == 'm')
     {
      digitalWrite (b_r_room, HIGH);
     }
     else if (value == 'n')
     {
      digitalWrite (b_r_room, LOW);
     }  
        
      else if (value == 'o')
      {
        digitalWrite (gard, HIGH);
      }
      else if (value == 'p')
      {
        digitalWrite (gard, LOW);
      } 

 //////////////////////////////PUERTAS//////////////////////////////

     if (value=='q')
     {
      puerta.write(10);
     }
     else if (value=='r')
     {
      puerta.write(90);
     }

   //------parking-----------
    voltaje_fotopark = analogRead(fotopark);
    if (value=='s')
    {
      parqueadero.write(0);
    }
    else if (value=='t')
    {
      parqueadero.write(96);
    }
    else if (value== 'z' && voltaje_fotopark>=umbralpark)
    {
      parqueadero.write(0);
      delay(3000);
    }
    else if (value== 'z' && voltaje_fotopark<umbralpark)
    {
      parqueadero.write(96);
    }


//////////////////////////////VENTILADOR//////////////////////////////
     else if (value =='w')
     {
      digitalWrite(ventilador,HIGH);
     }
     else if (value =='x')
     {
      digitalWrite(ventilador,LOW);
     }

//////////////////////////////ALARMA//////////////////////////////
 if (value=='u' && digitalRead(sensor) == LOW)
  {
     digitalWrite(LEDPin, HIGH);
     digitalWrite(buzzer,200); 
     delay(200); 
     digitalWrite(buzzer, LOW); 
     delay(200);
  }
  else if (value=='v')
  {
    digitalWrite(LEDPin, LOW);
    digitalWrite(buzzer, LOW);
  }
   }
