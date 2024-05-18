// el arduino posee un led interno en el circuito pin digital 13
int led = 13; // 2,3,4,5... 13

// el arduino tiene 4 pines digitales que van del 0 al 13
// sin embargo, cuando se utiliza comunicacion serial no se pueden utilizar
// los pines 0 y 1 como pines digitales

void setup() {
  // put your setup code here, to run once:
 // se debe defirnir el modo de trabajo e/s de todos los pines digitales
 pinMode(led, output);
}

void loop() {
  // put your main code here, to run repeatedly:
 digitalWrite(led, HIGH );
}
