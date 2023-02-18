
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
#define NO_COMMAND 8	
#define MAX_COMMAND NO_COMMAND

///Константы времени:
#define INIT_TIMEOUT 5000
#define DICE_TOWER_TIMEOUT 5000
#define CV_TIMEOUT 7000

///Переменные времени:
uint32_t drum_timeout = 10000;
uint32_t lift_timeout = 40000;

///Глобальные переменные:
int state = INIT_ST; ///хранит код текущего состояния системы

///////////////////////////////////////////////////////////////////////////////

void initSt_handler(int cmd){
	home();
	connect_dataBase();
	delay(INIT_TIMEOUT);
	state = WAITING_ST;
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
	drum_stop();
	drum_unload();
	delay(DICE_TOWER_TIMEOUT);
	CV_launch();
	delay(CV_TIMEOUT);
	lift_up();
	drum_moveLoad();
	drum_diceLoad();
	lift_down();
}

void drum_launch(){
	drumServo.write(DRUM_SPEED);
	delay(drum_timeout);
}

void lift_up(){
	liftServo.write(LIFT_SPEED);
	delay(lift_timeout);
}

void lift_up(){
	liftServo.write(LIFT_SPEED);
	delay(lift_timeout);
}	



///////////////////////////////////////////////////////////////////////////////

void setup() {
Serial.begin(115200);
}

int getCommand(){
	int cmd = NO_COMMAND;
	if (Serial.available()){
		cmd = Serial.read();
		if (cmd > SCANNING_ERR_CMD){
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
		case SYSTEM_START_STATE:{
		waitingSt_handler(cmd);
		break;
		}
		case NORMAL_MODE_STATE:{
		finiteModeSt_handler(cmd);
		break;
		}
		case INFINITE_MODE_STATE:{
		infiniteModeSt_handler(cmd);
		break;
		}
	}
}