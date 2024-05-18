//L298 - MODULO
// ---2 PUENTES H
// ENA, IN1, IN2, OUP1, OUT2 = VELOCIDAD DE GIRO, SENTIDO DE GIRO
// ENB, IN3 ,IN4, OUT3, OUT4 
int ENA = 3;  //PIN PM
int In1 = 5;
int In2 = 6;

//conectan al motor
//out 1 y 2 se conectan directamente del puente h al motor
  

void setup() {
  // put your setup code here, to run once:
  pinMode(In1, OUTPUT);
  pinMode(In2, OUTPUT);
  //ENA no lleva porque es PM
  Serial.begin(9600);
  Serial.setTime(10);

}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    int v = Serial.readString().toInt();
    if (v == 0){
      Serial.println("DETENERSE");
      digitalWrite(In1,0);
      digitalWrite(In2,0);
      digitalWrite(ENA,0);
    
    }
    else if(v==1){
      Serial.println("GIRAR IZQUIERA");
      digitalWrite(In1,0);
      digitalWrite(In2,0);
      digitalWrite(ENA,0);
    }
    else if(v==1){
      Serial.println("GIRAR DERECHA");
      digitalWrite(In1,0);
      digitalWrite(In2,0);
      digitalWrite(ENA,0);
    }
    else{
      Serial.println("MOVIMIENTO NO VALIDO");
      
    }
  }
  delay(100);
}
