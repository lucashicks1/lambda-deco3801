#include <Servo.h>
#include "pitches.h"

#define MESSAGE_OFFSET 3
#define SERVO_OFFSET 4
#define NUM_OF_SERVOS 4

// Define the digital pins for controlling
const int enableServo1 = 2;
const int enableServo2 = 3;
const int enableServo3 = 4;
const int enableServo4 = 5;
const int pwmBuzzerPin = 8; // PWM buzzer control pin
const int pwmServoPin = 9; // PWM servo control pin

char previousMessage[9] = ""; //Previous message

Servo servoSignal[NUM_OF_SERVOS]; //Array of servo controllers

/**
 * family_buzzer_writing(void) 
**/
void family_buzzer_writing(void) { //
  for (int i = 0; i < familyNotes * 2; i = i + 2) {

    // calculates the duration of each note
    divider = familyMelody[i + 1];
    if (divider > 0) {
      // regular note, just proceed
      familyNoteDuration = (wholenote) / divider;
    } else if (divider < 0) {
      // dotted notes are represented with negative durations!!
      familyNoteDuration = (wholenote) / abs(divider);
      familyNoteDuration *= 1.5; // increases the duration in half for dotted notes
    }

    // we only play the note for 90% of the duration, leaving 10% as a pause
    tone(pwmBuzzerPin, familyMelody[i], familyNoteDuration * 0.9);

    // Wait for the specief duration before playing the next note.
    delay(familyNoteDuration);

    // stop the waveform generation before the next note.
    noTone(pwmBuzzerPin);
  }
}

void buzzer_writing(int number) {
  for (int i = 0; i < numOfTones; i++) {
    int noteDuration = 1000 / userNoteDurations[number][i];
    int noteStartTime = millis();

    tone(pwmBuzzerPin, userMelody[number][i], noteDuration);

    // Wait for the note to finish playing
    delay(noteDuration);

    // Stop the tone playing
    noTone(pwmBuzzerPin);

    // Add a short pause between notes
    delay(50); // Adjust this value as needed
  }
  delay(1000);
}


void servo_write_cycle(char* message) {
  for (int i = SERVO_OFFSET; i < 8; i++) {
    int newPosition = (message[i] - '0') * 180; //Set angle for servo motor
    if (newPosition != servoSignal[i - SERVO_OFFSET].read()) { //If motor angle does not equal new angle
      servoSignal[i - SERVO_OFFSET].write(newPosition); //Write angle to servo
      if (newPosition == 0) {
        buzzer_writing(i - SERVO_OFFSET); //Write to buzzer
      }
      delay(500);
    } else {
      if (previousMessage[MESSAGE_OFFSET] == '1') { //Check if previous message was a family event and now not
        if (newPosition == 0) {
            buzzer_writing(i - SERVO_OFFSET);
        }
        delay(500);
      }
    }
  }
}

void servo_write_reset() {
  for (int i = MESSAGE_OFFSET; i < 8; i++) {
    int newPosition = 0;
    if (newPosition != servoSignal[i - SERVO_OFFSET].read()) {
      servoSignal[i - SERVO_OFFSET].write(newPosition);
    }
  }
}

void setup() {
  // Initialize serial communication
  Serial.begin(9600);

  servoSignal[0].attach(enableServo1);
  servoSignal[1].attach(enableServo2);
  servoSignal[2].attach(enableServo3);
  servoSignal[3].attach(enableServo4);

  // Set PWM pin as an output
  pinMode(pwmServoPin, OUTPUT);
  pinMode(pwmBuzzerPin, OUTPUT);
  digitalWrite(pwmServoPin, LOW);
}

void loop() {
  if (Serial.available() >= 😎 { // Check if there are at least 8 characters available in the serial buffer
    char currentMessage[9]; // Buffer to store the received message
    Serial.readBytes(currentMessage, 8); // Read the message into the buffer
    currentMessage[8] = '\0'; // Null-terminate the string
    analogWrite(pwmServoPin, 255); // Set PWM duty cycle to maximum (255) on pin 9

    if (strncmp(currentMessage, previousMessage, 😎 != 0) {
      if ((currentMessage[MESSAGE_OFFSET] == '1')) {
        if((currentMessage[MESSAGE_OFFSET] != previousMessage[MESSAGE_OFFSET])) {
          servo_write_reset();
          family_buzzer_writing();
        }
        delay(1000);
      } else {
        servo_write_cycle(currentMessage);
        delay(1000);
      }
      strncpy(previousMessage, currentMessage, 8);
    }

    analogWrite(pwmServoPin, 0); // Turn off PWM on pin 9
  }
}