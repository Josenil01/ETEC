pp#include <WiFi.h>
#include <HTTPClient.h>
#include <math.h>

// Configurações do Wi-Fi simulado do Wokwi
const char* ssid = "Wokwi-GUEST";
const char* password = "";

// CONFIGURAÇÃO DO THINGSPEAK (Alunos substituem aqui)
String channelID = "2468101";           // Substituir pelo ID do Canal do ThingSpeak
String writeAPIKey = "XYZ123ABC456";    // Substituir pela Write API Key do ThingSpeak

unsigned long lastTime = 0;
unsigned long timerDelay = 15000; // O ThingSpeak gratuito exige intervalo mínimo de 15 segundos

void setup() {
  Serial.begin(115200);
  randomSeed(analogRead(0));

  Serial.print("Conectando ao Wi-Fi");
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nConectado ao Wi-Fi!");
}

void loop() {
  if ((millis() - lastTime) > timerDelay) {
    if (WiFi.status() == WL_CONNECTED) {
      
      // 1. MANIPULAÇÃO DE NÚMEROS ALEATÓRIOS
      float ruido = random(-200, 200) / 100.0; 

      // 2. FUNÇÕES TRIGONOMÉTRICAS
      float angulo = millis() / 20000.0; 
      float componenteSazonal = sin(angulo) * 10; 

      // 3. FUNÇÕES MATEMÁTICAS BÁSICAS
      float temperaturaFinal = 25.0 + componenteSazonal + ruido;

      // Exibição no monitor serial para validação do professor
      Serial.print("Temperatura calculada para envio: ");
      Serial.println(temperaturaFinal);

      // Envio para o ThingSpeak via requisição HTTP simples
      HTTPClient http;
      
      // O ThingSpeak recebe dados passando "field1=", "field2=", etc. na URL
      String url = "http://thingspeak.com" + writeAPIKey + 
                   "&field1=" + String(temperaturaFinal) + 
                   "&field2=" + String(componenteSazonal);
      
      http.begin(url);
      int httpResponseCode = http.GET(); // Envio simples usando GET
      
      if (httpResponseCode > 0) {
        Serial.print("ThingSpeak atualizado! Código de resposta: ");
        Serial.println(httpResponseCode);
      } else {
        Serial.print("Erro no envio: ");
        Serial.println(httpResponseCode);
      }
      http.end();
    }
    lastTime = millis();
  }
}