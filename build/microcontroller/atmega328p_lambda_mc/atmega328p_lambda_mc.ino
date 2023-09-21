#include <Servo.h>
#include "pitches.h"

#define MESSAGE_OFFSET 3
#define SERVO_OFFSET 4
#define NUM_OF_SERVOS 4

// Define the digital pins for controlling
const int enableServoPins[] = {3, 5, 6, 9};
const int pwmBuzzerPin = 8; // PWM buzzer control pin

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
  for (int i = 0; i < NUM_OF_SERVOS; i++) {
    int newPosition = ((message[i + SERVO_OFFSET] - '0') * 180); // Set angle for servo motor
    if (message[i + SERVO_OFFSET] != previousMessage[i + SERVO_OFFSET]) { // If motor angle does not equal new angle
      servoSignal[i].write(newPosition); // Write angle to servo
      if (newPosition == 0) {
        buzzer_writing(i); // Write to buzzer
      }
      delay(500);
    } else {
      if (previousMessage[MESSAGE_OFFSET] == '1') { // Check if previous message was a family event and now not
        if (newPosition == 0) {
          buzzer_writing(i);
        }
        delay(500);
      }
    }
  }
}

void servo_write_reset() {
  for (int i = 0; i < NUM_OF_SERVOS; i++) {
    int newPosition = 0;
    if (newPosition != servoSignal[i].read()) {
      servoSignal[i].write(newPosition);
    }
  }
}

void setup() {
  // Initialize serial communication
  Serial.begin(9600);

  for(int n = 0; n < NUM_OF_SERVOS; n++) {
    servoSignal[n].attach(enableServoPins[n]);
    servoSignal[n].write(180);
  }

  pinMode(pwmBuzzerPin, OUTPUT);
}

void loop() {
  if (Serial.available() >= 8) { // Check if there are at least 8 characters available in the serial buffer
    char currentMessage[9]; // Buffer to store the received message
    Serial.readBytes(currentMessage, 8); // Read the message into the buffer
    currentMessage[8] = '\0'; // Null-terminate the string

    if (strncmp(currentMessage, previousMessage, 8) != 0) {
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

  }
}