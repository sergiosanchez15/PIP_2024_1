

void setup() {
  // put your setup code here, to run once:
  //mudulo uart... modulo asincrono unversal  de transmision y recepcion de datos
  Serial.begin(9600); //INICIALIZA LA COMUNIACION SERIAL...
  //9600  son los baudios a los que se comunica con otros dispositivos...
  //arduino trabaa a 16mhz por segundo...
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("HOLA :D! ;3");
  delay(500); //milsecs

}
