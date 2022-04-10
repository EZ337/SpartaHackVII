//Temperature, Humidity Sensor, pressure and light sensor 
#include "DHT.h"
#include <Arduino.h>
#include <U8x8lib.h>
#include "Seeed_BMP280.h"
#include <Wire.h>
#include <Servo.h>

int sensorpin=A6;
int ledPin = 4;    
int sensorval = 0;        
int outputValue = 0;  
Servo myservo;      


BMP280 bmp280;
 
#define DHTPIN 3     // what pin we're connected to
#define DHTTYPE DHT11   // DHT 11 
DHT dht(DHTPIN, DHTTYPE);
 
U8X8_SSD1306_128X64_NONAME_HW_I2C u8x8(/* reset=*/ U8X8_PIN_NONE);

int BuzzerPin = 5;
const int LEDlightPin =  4;
int pos =0;
 
void setup(void) {
  Serial.begin(9600); 
  Serial.println("DHTxx test!");
  dht.begin();
  u8x8.begin();
  u8x8.setPowerSave(0);  
  u8x8.setFlipMode(1);
  
  pinMode(sensorpin, INPUT);
  pinMode(BuzzerPin, OUTPUT);
  pinMode(LEDlightPin, OUTPUT);
  myservo.attach(10);
}
 
void loop(void) {
 
  float temperature, humidity;
  temperature = dht.readTemperature(); // takes the temperature reading
  humidity = dht.readHumidity(); // takes the humidity reading
  float pressure;
 
  u8x8.setFont(u8x8_font_chroma48medium8_r);
  u8x8.setCursor(0, 33);
  u8x8.print("Temp :");
  u8x8.print(temperature);
  u8x8.print("C");
  Serial.print(" Current temperature is ");
  Serial.print(temperature);
  u8x8.setCursor(0,50);

  if (temperature>60) {          // loop to check if temperature is in range and if not then the buzzer rings
    analogWrite(BuzzerPin, 128);
  } else if (temperature<10) {
    analogWrite(BuzzerPin, 128);
  } else {
    analogWrite(BuzzerPin, 0);
  }
  
  u8x8.print("Humidity:");
  u8x8.print(humidity);
  
  if (humidity>50) {              // loop to check if humidity is in range and if not then the buzzer rings
    analogWrite(BuzzerPin, 128);
    
  } else if (humidity<10) {
    analogWrite(BuzzerPin, 128);
    
  } else {
    analogWrite(BuzzerPin, 0);
    
  }
  Serial.print(" Current humidity is ");
  Serial.print(humidity);
  u8x8.print("%");

  Serial.print(" Pressure: ");
  pressure = bmp280.getPressure();
  pressure = pressure+101;
  Serial.print(pressure);
  Serial.print(" KPa ");

  sensorval=analogRead(sensorpin);
  Serial.print(" Light intensity value: ");
  Serial.println(sensorval);

  if (sensorval<250){
    digitalWrite(LEDlightPin, HIGH);
    
  } else {
    digitalWrite(LEDlightPin, LOW);
    
  }

  

  
  u8x8.refreshDisplay();
  delay(200);
}
