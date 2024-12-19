#include <Servo.h>

Servo servo;

void setup(){
  Serial.begin(9600);
  servo.attach(9);
}
void loop(){
  if(Serial.available() > 0){
    String angleString = Serial.readStringUntil("\n");
    int angle = angleString.toInt();

    servo.write(angle);
  }
}