
	 /////______/////
	///__///_///____//
   ///_____///______//
   //_______________//
    //_____________//
	 ///_________///
	  ////_____////
	    ///___///
		  //_//
		   ///
			/
			
///Импортированные библиотеки
#include <Servo.h>

///Подключения:
#define PIN_DRUM 1
Servo liftServo;
int carriage = 3;

///Константы-состояния:
#define INIT_ST 0
#define WAITING_ST  1
#define FINITE_MODE_ST 2
#define INFINITE_MODE_ST 3
#define DRUM_LAUNCH_ST 4
#define DRUM_LOAD_ST 5
#define LIFT_UP_ST 6
#define LIFT_DOWN_ST 7
#define CV_LAUNCH_ST 8

///Константы команды:
#define FINITE_LAUCH_COMMAND 0
#define INFINITE_LAUNCH_COMMAND 1
#define DRUM_LAUNCH_COMMAND 2
#define DRUM_LOAD_COMMAND 3
#define LIFT_UP_COMMAND 4
#define LIFT_DOWN_COMMAND 5
#define CV_LAUNCH_COMMAND 6
#define STOP_COMMAND 7
#define UNLOAD_COMMAND 8
#define UPLOAD_COMMAND 9
#define NO_COMMAND 10	
#define MAX_COMMAND NO_COMMAND

///Константы времени:
#define INIT_TIMEOUT 5000
#define DICE_TOWER_TIMEOUT 5000
#define CV_TIMEOUT 7000
#define DRUM_LOAD_TIMEOUT 4000
#define LIFT_TIMEOUT 55000

///Константы скорости:
#define DRUM_SPEED 100
#define LIFT_SPEED 200

///Переменные времени:
uint32_t drum_timeout = 10000;

///Глобальные переменные:
int state = INIT_ST; //хранит код текущего состояния системы
bool conState = false; //показывает подключение к базе данных

///////////////////////////////////////////////////////////////////////////////

void initSt_handler(int cmd){
	home();
	connect_dataBase();
	delay(INIT_TIMEOUT);
	state = WAITING_ST;
}

void connect_dataBase(){
	conState = true;
}

void waitingSt_handler(int cmd){
	switch(cmd){
		case LIFT_UP_COMMAND:{
			state=LIFT_UP_ST;
			break;
		}
		case LIFT_DOWN_COMMAND:{
			state = LIFT_DOWN_ST;
			break;
		}
		case CV_LAUNCH_COMMAND:{
			state=CV_LAUNCH_ST;
			break;
		}
		case DRUM_LOAD_COMMAND:{
			state = DRUM_LOAD_ST;
			break;
		}
		case DRUM_LAUNCH_COMMAND:{
			state=DRUM_LAUNCH_ST;
			break;
		}
		case INFINITE_LAUNCH_COMMAND:{
			state = INFINITE_MODE_ST;
			break;
		}
		case FINITE_LAUCH_COMMAND:{
			state = FINITE_MODE_ST;
			break;
		}
	}
}
	
void finiteModeSt_handler(int cmd, int count){
	int i = 0;
	if (cmd == STOP_COMMAND){
		for (i, i<count, i+=1){
			if (!(delayedStop)){
				launch_cycle();
			}
		}
		else{
			state = WAITING_ST;
			home();
		}
	}
	else{
		state = WAITING_ST;
		home();
	}
}

void infiniteModeSt_handler(int cmd, int count){
	if (cmd != STOP_COMMAND){
		while (!(delayedStop)){
				launch_cycle();
		}
		state = WAITING_ST;
		home();
	}
	else{
		state = WAITING_ST;
		home();
	}
}

void launch_cycle(){
	drum_launch();
	CV_launch();
	delay(CV_TIMEOUT);
	drum_load();
	lift_up();
	lift_down();
}

/// launch_cycle подфункции
void drum_launch(){
	// Плавно разгоняем двигатель
	for(uint32_t i = 0; i < DRUM_SPEED; i++) {
		analogWrite(PIN_DRUM, i);
		delay(20);
	}
	drum_timeout = Serial.read()
	delay(drum_timeout); // Двигатель работает drum_timeout на полную мощность
	while (cmd!=UNLOAD_COMMAND){
		analogWrite(PIN_DRUM, DRUM_SPEED);
	}
	// Плавно тормозим двигатель
	for(uint32_t i = DRUM_SPEED; i < 0; i--) {
		analogWrite(PIN_DRUM, i);
		delay(20);
	}
	delay(DICE_TOWER_TIMEOUT);
}

void CV_launch(){
	while (cmd!=CV_LAUNCH_COMMAND){
		Serial.print();
	}
}

void drum_load(){
	while (cmd!=UPLOAD_COMMAND){
		analogWrite(PIN_DRUM, DRUM_SPEED);
	}
	delay(DRUM_LOAD_TIMEOUT);
}

void lift_up(){
	setMaxSpeed(LIFT_SPEED);
	delay(LIFT_TIMEOUT);
	liftServo.write(135);
	liftServo.write(90);
	delay(LIFT_TIMEOUT);
}

void lift_down(){
	reverse(true);
	setMaxSpeed(LIFT_SPEED);
	delay(LIFT_TIMEOUT);
}

void home(){
	drum_load();
	lift_down();
}

///////////////////////////////////////////////////////////////////////////////

void setup(){
	Serial.begin(115200);
	liftServo.attach(2);
	pinMode(carriage, OUTPUT);
}

int getCommand(){
	int cmd = NO_COMMAND;
	if (Serial.available()){
		cmd = Serial.read();
		if (cmd > MAX_COMMAND){
			int cmd = NO_COMMAND;
		}
		else{
			return cmd;
		}
	}
	return cmd;
}

void loop(){
	int cmd = getCommand();
	switch(state){
		case INIT_ST:{
		initSt_handler(cmd);
		break;
		}
		case WAITING_ST:{
		waitingSt_handler(cmd);
		break;
		}
		case FINITE_MODE_ST:{
		finiteModeSt_handler(cmd);
		break;
		}
		case INFINITE_MODE_STATE:{
		infiniteModeSt_handler(cmd);
		break;
		}
		case DRUM_LAUNCH_ST:{
		drum_launch(cmd);
		break;
		}
		case DRUM_LOAD_COMMAND:{
		drum_load(cmd);
		break;
		}
		case LIFT_UP_ST:{
		lift_up(cmd);
		break;
		}
		case LIFT_DOWN_ST:{
		lift_down(cmd);
		break;
		}
		case CV_LAUNCH_ST:{
		CV_launch(cmd);
		break;
		}
	}
}