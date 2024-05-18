int revelador = 13;

void setup() {
  // put your setup code here, to run once:
  pinMode(revelador, OUTPUT);
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()>0){
  int v = Serial.readString().toInt();
  digitalWrite(revelador, v);
  Serial.print("ESTADO APLICADO:" + String(v));
  }
  delay(100);
} 
