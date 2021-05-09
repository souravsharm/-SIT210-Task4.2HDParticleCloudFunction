int orange = D1; 
int yellow = D2;  
int green = D3; 


void setup()
{


   pinMode(orange, OUTPUT);
   pinMode(yellow, OUTPUT);
   pinMode(green, OUTPUT);
   
   Particle.function("led",ledToggle);

   digitalWrite(orange, LOW);
   digitalWrite(yellow, LOW);
   digitalWrite(green, LOW);

}




void loop()
{

}


int ledToggle(String command){
    

    if (command=="orangenon") {
        digitalWrite(orange,HIGH);
        digitalWrite(yellow,LOW);
        digitalWrite(green,LOW);
        return 1;
    }
    else if (command=="yellowon") {
        digitalWrite(orange,LOW);
        digitalWrite(yellow,HIGH);
        digitalWrite(green,LOW);
        return 0;
    }
    else if (command=="greenon") {
        digitalWrite(orange,LOW);
        digitalWrite(yellow,LOW);
        digitalWrite(green,HIGH);
        return 0;
    }
    else {
        return -1;
    }
}