#include <Servo.h>

// Define the digital pins for microcontroller use
const int enableServo1 = 2;
const int enableServo2 = 3;
const int enableServo3 = 4;
const int enableServo4 = 6;
const int pwmPin = 9; // PWM control pin

char previousMessage[9] = "";

//Use servo library
Servo servoSignal1;
Servo servoSignal2;
Servo servoSignal3;
Servo servoSignal4;

void setup() {
  // Initialize serial communication
  Serial.begin(9600);

  //Attach servo enable pins
  servoSignal1.attach(enableServo1);
  servoSignal2.attach(enableServo2);
  servoSignal3.attach(enableServo3);
  servoSignal4.attach(enableServo4);
  //Write angle of servos to 0
  servoSignal1.write(0);
  servoSignal2.write(0);
  servoSignal3.write(0);
  servoSignal4.write(0);

  // Set PWM pin as an output
  pinMode(pwmPin, OUTPUT);
  digitalWrite(pwmPin, LOW);
}

void loop() {
  if (Serial.available() >= 8) { // Check if there are at least 8 characters available in the serial buffer
    char currentMessage[9]; // Buffer to store the received message
    Serial.readBytes(currentMessage, 8); // Read the message into the buffer
    currentMessage[8] = '\0'; // Null-terminate the string

    if (strncmp(currentMessage, previousMessage, 8) != 0) {
      if (currentMessage[3] == '1') {
        analogWrite(pwmPin, 255); // Set PWM duty cycle to maximum (255) on pin 9
        servoSignal1.write(0);
        servoSignal2.write(0);
        servoSignal3.write(0);
        servoSignal4.write(0);
        delay(1000);
        analogWrite(pwmPin, 0); // Turn off PWM on pin 9
      } else {
        analogWrite(pwmPin, 255); // Set PWM duty cycle to maximum (255) on pin 9
        servoSignal1.write((currentMessage[4] - '0') * 180);
        servoSignal2.write((currentMessage[5] - '0') * 180);
        servoSignal3.write((currentMessage[6] - '0') * 180);
        servoSignal4.write((currentMessage[7] - '0') * 180);
        delay(1000);
        analogWrite(pwmPin, 0); // Set PWM duty cycle to maximum (255) on pin 9
      }
      strncpy(previousMessage, currentMessage, 8);
    }
  }
}