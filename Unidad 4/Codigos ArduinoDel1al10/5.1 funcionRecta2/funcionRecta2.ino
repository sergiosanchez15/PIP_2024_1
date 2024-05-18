double x1, y1, x2, y2, m, b, x, y;

double obtenerValor(String msg){
  Serial.print(msg);
  while(Serial.available() == 0){}
  double valor = Serial.readString().toDouble();
  Serial.println(" " + String(valor));
  return valor;
}

void setup() {
  Serial.begin(9600);
}

void loop() {
  x1 = obtenerValor("Ingrese el valor de x1...:");
  y1 = obtenerValor("Ingrese el valor de y1...:");
  x2 = obtenerValor("Ingrese el valor de x2...:");
  y2 = obtenerValor("Ingrese el valor de y2...:");

  m = (y2 - y1) / (x2 - x1);
  b = y1 - m * x1;
  Serial.println("Funcion de la recta es : y = " + String(m) + "x + (" +  String(b) + ")");
}
