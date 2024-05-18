//L298 - MODULO
// ---2 PUENTES H
// ENA, IN1, IN2, OUP1, OUT2 = VELOCIDAD DE GIRO, SENTIDO DE GIRO
// ENB, IN3 ,IN4, OUT3, OUT4 
int ENA = 3;  //PIN PM
int In1 = 13;
int In2 = 12;

//conectan al motor
//out 1 y 2 se conectan directamente del puente h al motor
  

void setup() {
  // put your setup code here, to run once:
  pinMode(In1, OUTPUT);
  pinMode(In2, OUTPUT);
  //ENA no lleva porque es PM
  Serial.begin(9600);
  Serial.setTimeout(10);

}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    int v = Serial.readString().toInt();
      digitalWrite(In1,1); // donde el output 1 esta conectado a un led
      analogWrite(ENA, v); // v debe de ir de 0 a 255
  }
  delay(100);
}
