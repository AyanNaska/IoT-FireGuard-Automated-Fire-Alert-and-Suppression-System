from gpio import*
from time import*
def main ( );
      pinMode(0,INPUT)   # For the fire detector
      pinMode(1,OUT)      #For the sprinkler
      pinMode(2,OUT)      #For the Speaker
      pinMode(3,OUT)      #For the emergency door
      pinMode(4,OUT)      #For LCD Display
while True:       #Looping to keep the program running
           fire=digitalRead(0);
           if(fire==1023):     #1023 is the value detected by the sensor
               customWrite(1,’1’);                   #command to turn on the sprinkler
               digitalWrite(2,HIGH);                #command to turn on the speaker
               customWrite(3,HIGH);               #command to activate door
               customWrite(4,”FIRE DETECTED”);#command to print the message on lcd panel 
           else:
               customWrite(1,’0’);        #command to turn off the sprinkler
               digitalWrite(2,LOW);      #command to turn off the speaker
               customWrite(3,LOW);     #command to close the door
               customWrite(4,”SAFE”);  #command to print the message on lcd pannel
if__name__ ==”__main__”: