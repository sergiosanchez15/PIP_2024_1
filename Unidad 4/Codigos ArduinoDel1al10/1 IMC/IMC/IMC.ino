#include <Arduino.h>

float peso, altura, imc;

void setup() {
  Serial.begin(9600);
}

void loop() {
  // Solicitar al usuario que ingrese su peso en kg
  Serial.println("Ingrese su peso en kilogramos:");
  while (!Serial.available()) {}
  peso = Serial.parseFloat();

  // Esperar un poco para que el usuario pueda ingresar el valor
  delay(100);

  // Solicitar al usuario que ingrese su altura en metros
  Serial.println("Ingrese su altura en metros:");
  while (!Serial.available()) {}
  altura = Serial.parseFloat();

  // Calcular el IMC
  imc = peso / (altura * altura);

  // Mostrar el resultado
  Serial.print("Su IMC es: ");
  Serial.println(imc);

  // Interpretar el IMC
  if (imc < 18.5) {
    Serial.println("Bajo peso");
  } else if (imc < 25) {
    Serial.println("Peso normal");
  } else if (imc < 30) {
    Serial.println("Sobrepeso");
  } else {
    Serial.println("Obesidad");
  }

  // Esperar un poco antes de repetir el ciclo
  delay(5000);
}
