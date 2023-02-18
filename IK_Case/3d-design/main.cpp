#include <Arduino.h>

#include "painlessMesh.h"
#include <Adafruit_Sensor.h>
#include <Arduino_JSON.h>
#include <DHT.h>
#include <DHT_U.h>
#include <cmath>

#define SOIL_MOISTURE A0
#define DHTPIN D5
#define DHTTYPE DHT11

#define MESH_PREFIX "RNTMESH" // имя MESH
#define MESH_PASSWORD "MESHpassword" // пароль

#define MESH_PORT 5555 // порт по умолчанию

DHT_Unified dht(DHTPIN, DHTTYPE); //объект для датчика DHT11
	
int nodeNumber = 1;//уникальный номер ноды платы
	
Scheduler userScheduler;//планировщик
painlessMesh  mesh;//объект сети mesh
String readings;//сохраняем показания сюды

void sendMessage() ; // благодаря ему PlatformIO будет работать
 
String getReadings(); // получение показаний датчика
Task taskSendMessage(TASK_SECOND * 10 , TASK_FOREVER, &sendMessage);//каждые 10 сек ПОСТОЯННО передает сообщение
String getReadings () {//Функция getReadings () получает показания температуры, влажности и давления от датчика 
// и объединяет всю информацию, включая номер ноды, в переменной jsonReadings.
  //uint32_t now = millis();
  sensors_event_t event;
  JSONVar jsonReadings;
  jsonReadings["node"] = nodeNumber;
  dht.temperature().getEvent(&event);
  jsonReadings["temp"] = event.temperature;
  dht.humidity().getEvent(&event);
  jsonReadings["hum"] = event.relative_humidity;
  jsonReadings["soil_hum"] = analogRead(SOIL_MOISTURE);

  //last_sensor_read = millis();
  readings = JSON.stringify(jsonReadings);//значения переменной jsonReadings преобразуется в строку JSON
    //и сохраняется в переменной readings.
  return readings;
  
}

void sendMessage (){//отправляет строку JSON с показаниями и номером ноды (getReadings ()) ВСЕМ нодам в сети.
  String msg = getReadings();
  mesh.sendBroadcast(msg);
}

// Нужно для работы библиотеки painlessMesh
 
void receivedCallback( uint32_t from, String &msg ) {//выводит отправителя сообщения и содержимое сообщения (msg.c_str ())
  Serial.printf("Received from %u msg=%s\n", from, msg.c_str());
  JSONVar myObject = JSON.parse(msg.c_str());
  String received = JSON.stringify(myObject);
  Serial.print(received);
}
 
 
 
void newConnectionCallback(uint32_t nodeId) {//работает,когда к сети подключается новая нода
  Serial.printf("New Connection, nodeId = %u\n", nodeId);
}
 
 
 
void changedConnectionCallback() {//когда соединение изменяется в сети (когда узел присоединяется к сети или покидает ее).
  Serial.printf("Changed connections\n");
}
 
 
 
void nodeTimeAdjustedCallback(int32_t offset) {//запускается, когда сеть регулирует время,
// так что все узлы синхронизируются. Печатает смещение.
  Serial.printf("Adjusted time %u. Offset = %d\n", mesh.getNodeTime(),offset);
}
 
void setup() {

  Serial.begin(115200);
  dht.begin();
  //mesh.setDebugMsgTypes( ERROR | MESH_STATUS | CONNECTION | SYNC | COMMUNICATION | GENERAL | MSG_TYPES | REMOTE ); // выбираем типы  mesh.setDebugMsgTypes( ERROR | STARTUP );  // установите перед функцией init() чтобы выдавались приветственные сообщения
  mesh.init( MESH_PREFIX, MESH_PASSWORD, &userScheduler, MESH_PORT );
  mesh.onReceive(&receivedCallback);
  mesh.onNewConnection(&newConnectionCallback);
  mesh.onChangedConnections(&changedConnectionCallback);
  mesh.onNodeTimeAdjusted(&nodeTimeAdjustedCallback); 

  userScheduler.addTask(taskSendMessage);//Планировщик отвечает за обработку и выполнение задач в нужное время.
  taskSendMessage.enable();//стартуем
}
 
 
 
void loop() {
// функция также запустит планировщик
  mesh.update();
}
