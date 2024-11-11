#include <LiquidCrystal.h>


const int rs = 6, en = 7, d4 = 8, d5 = 9, d6 = 10, d7 = 11;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
int num=0;
int leduse=13;
                

void setup(void) {
  Serial.begin(9600);  
  lcd.begin(16, 2);
  pinMode(13, OUTPUT);                        
}

String serialReceive;                        
String CPUstat;


void loop(void) {
  
  if(Serial.available() > 0) {                
    serialReceive = Serial.readString();      
  }
 lcd.clear();

  CPUstat = serialReceive.substring(0, 5);    
 
  num=CPUstat.toInt();
  lcd.setCursor(8,0);
  lcd.print(CPUstat);
   lcd.setCursor(0,0);
  lcd.print("CPU:");
  lcd.setCursor(0,1);
  lcd.print("HEAVY KODER :)");
  if(leduse<13){
    delay(1000);
    leduse++;
  }
  
   num=CPUstat.toInt();
   
  
  if(num>30){
    digitalWrite(13, HIGH);
    leduse=0;
  }
  if(leduse>12&&num<30){
    digitalWrite(13, LOW);
  }
}