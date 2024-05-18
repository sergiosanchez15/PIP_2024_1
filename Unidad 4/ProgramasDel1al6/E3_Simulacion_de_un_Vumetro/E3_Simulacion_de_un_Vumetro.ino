int valor;
#define ledRojo 2
#define ledNaranja 3
#define ledAmarrillo 4
#define ledVerde 5
#define ledAzul 6

void setup()
{
  Serial.begin(9600);
  pinMode(ledRojo, OUTPUT);
  pinMode(ledNaranja, OUTPUT);
  pinMode(ledAmarrillo, OUTPUT);
  pinMode(ledVerde, OUTPUT);
  pinMode(ledAzul, OUTPUT);
}

void loop()
{
  valor = analogRead(A0);
  Serial.println("Valor del potenciometro: " + String(valor));
  if(valor > 0) digitalWrite(ledAzul,HIGH);
  else digitalWrite(ledAzul,LOW);
                 
  if(valor > 205) digitalWrite(ledVerde,HIGH);
  else digitalWrite(ledVerde,LOW);
                 
  if(valor > 410) digitalWrite(ledAmarrillo,HIGH);
  else digitalWrite(ledAmarrillo,LOW);
                 
  if(valor > 615) digitalWrite(ledNaranja,HIGH);
  else digitalWrite(ledNaranja,LOW);
                 
  if(valor > 820) digitalWrite(ledRojo,HIGH);
  else digitalWrite(ledRojo,LOW);
}