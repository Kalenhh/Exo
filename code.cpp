// code.cpp
// Projet Pince sensible 1g1

#include <Servo.h>

int entry_servo = 2 ;           //
int entry_capteur = 0 ;         //Entré Pin
int entry_joystick = 1 ;        //

int max_capacity = 400 ;        //
int min_capacity = 350 ;        //Valeur de pression de la pince sur le capteur de force

float servo_position = 90.0 ;   //Position du servomoteur
int joystick_position = 0 ;     //Position du joystick

bool security = true ;          //Option
int sensibility = 1 ;           //

Servo main_servo ;              //

void setup(){
  main_servo.attach(entry_servo);
  pinMode(entry_capteur,INPUT);
  pinMode(entry_joystick,INPUT);

  Serial.begin(9600);
}

void loop(){
  main_servo.write(servo_position);       //actualisation de la position de la pince
  
  int joystick_position = analogRead(entry_joystick) ;    //On lit les entrées analogiques
  int force_capteur = analogRead(entry_capteur) ;
  
  Serial.println(servo_position) ;

  if (joystick_position > 500){         //La pince s'ouvre
    if (force_capteur < max_capacity and servo_position < 170 or force_capteur => max_capacity and security == false){
      servo_position = servo_position + 0.1*sensibility;
    }

  }
  if (joystick_position < 200){         //La pince ferme
    if (servo_position >10){
      servo_position = servo_position - 0.1*sensibility;
    }
  }

  if (joystick_position = 701){         //(des)activer la sécurité
    security = !security;
    delay(1)
}




"""


void setup(){
  pinMode(0,INPUT) ;   // analog
  pinMode(4,OUTPUT) ;  // del rouge
  pinMode(2,OUTPUT) ;  // del verte

  Serial.begin(9600) ;
}

void loop(){

  float mesure = analogRead(0) ;
  mesure = mesure / 686 * 1024;
  Serial.println(mesure) ;

  if (mesure <= 256 or mesure >= 768){      // plage 1 et 3
    digitalWrite(4,HIGH) ;
    digitalWrite(2,LOW) ;
  }

  if (mesure > 256 and mesure < 768){       // plage 2
    digitalWrite(4,LOW) ;
    digitalWrite(2,HIGH) ;
  }
}

"""

"""

void setup(){
  pinMode(0,INPUT) ;   // analog
  pinMode(4,OUTPUT) ;  // del rouge
  pinMode(2,OUTPUT) ;  // del verte

  Serial.begin(9600) ;
}

void loop(){

  float mesure = analogRead(0) ;
  mesure = mesure / 686 * 1024 * 2;
  Serial.println(mesure) ;

  delay(mesure) ;
  digitalWrite(4,HIGH) ;
  digitalWrite(2,LOW) ;

  delay(mesure) ;
  digitalWrite(2,HIGH) ;
  digitalWrite(4,LOW) ;

"""