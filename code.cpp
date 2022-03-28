//code

#include <Servo.h>

int entry_servo = 2 ;
int entry_capteur = 0 ;			//Entré Pin
int entry_joystick = 1 ;

int max_capacity = 400 ;
int min_capacity = 350 ;		//Valeur de pression de la pince sur le capteur de force

float servo_position = 90.0 ;	//Position du servomoteur



bool security = true ;			//Option
int sensibility = 1 ;

Servo main_servo ;

void setup(){
	main_servo.attach(entry_servo);
	pinMode(entry_capteur,INPUT);
	pinMode(entry_joystick,INPUT);

	Serial.begin(9600);
}

void loop(){

	main_servo.write(servo_position)	//actualisation de la position de la pince
	
	if (analogRead(entry_joystick) > 500){
		if (analogRead(entry_capteur) >= max_capacity and security == true or main_servo.read() >= 170){
			continue ;
		}

		servo_position = servo_position + 0.1*sensibility;
	}
	if (analogRead(entry_joystick) < 200){
		if (main_servo.read() <=10){
			continue ;
		}

		servo_position = servo_position - 0.1*sensibility;
	}
}