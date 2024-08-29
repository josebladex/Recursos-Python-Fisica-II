/****************************************************************************************
 *                                Proyecto Final Fisica II                             *
 *                            Universidad de Panamá - José Plata    *
 **************************************************************************************/
// Definición de pines utilizados en el programa
#define pinAnalogo    0      
#define pinCarga      13     
#define pinDescarga   8      

// Variables para medir el tiempo
unsigned long tiempoInicio;
unsigned long tiempoTranscurrido;

void setup() {
  pinMode(pinCarga, OUTPUT);         // Establece el pin de carga como salida digital
  digitalWrite(pinCarga, LOW);       // Apaga la carga del condensador al principio
  Serial.begin(9600);                // Inicializa la comunicación serial a 9600 baudios
  Serial.println("Medición de Capacitancia"); // Imprime mensaje de inicio
}


void loop() {
  // Descarga completa del condensador
  pinMode(pinDescarga, OUTPUT);       // Establece el pin de descarga como salida
  digitalWrite(pinDescarga, LOW);     // Pone el pin de descarga en bajo

  Serial.println("Descargando Capacitor ..."); 
  
  // Espera hasta que el voltaje en el pin analógico sea 0
  while (analogRead(pinAnalogo) > 0) {
    // Imprime el valor del pin analógico durante la descarga
    Serial.print("Valor de pinAnalogo en DESCARGA: ");
    Serial.println(analogRead(pinAnalogo));
  }
  
  pinMode(pinDescarga, INPUT); // Establece el pin de descarga en alta impedancia
  
  tiempoInicio = micros(); // Registra el tiempo de inicio de carga
  digitalWrite(pinCarga, HIGH); // Activa la carga del condensador
  Serial.println("Datos para análisis Gráfico: "); 
  
  // 1019 equivale a aproximadamente el 99% de la carga del condensador

int i = 1;

  while (analogRead(pinAnalogo) < 1019) { 
    // Imprime el valor del pin analógico durante la carga
    if(i == 1)
    Serial.print("{tiempo:");
    else
    Serial.print(",tiempo:");
    tiempoTranscurrido = micros() - tiempoInicio;
    Serial.print((float)tiempoTranscurrido / 1000000.0);
    Serial.print(",voltaje:");
    Serial.print((float)analogRead(pinAnalogo) / 1023 * 5, 3);
    i++;
  }
  
  Serial.println("}"); // Imprime resultados en JSON
  digitalWrite(pinCarga, LOW); // Detiene la carga del condensador
}