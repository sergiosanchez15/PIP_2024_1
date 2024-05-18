int v;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){ //comprueba el bufer del arduino
     //readString leeara todos los bytes posibles antes de que
     //se acabe su tiempo de espera (timeout)
     //por defecto el timeout es de 1 segundo
    v = Serial.readString().toInt();
    Serial.println(v);
  }

}
