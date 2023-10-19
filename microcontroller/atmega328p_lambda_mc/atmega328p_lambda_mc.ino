/**
  ******************************************************************************
  * @file    atmega328p_lambda_mc.ino
  * @author  Dylan Fleming - 45313345
  * @brief   Microcontroller code for Team \Lamdba Installation
  ******************************************************************************
**/

/*=============================== INCLUDES ===============================*/
#include <Servo.h>
#include "pitches.h"

/*=============================== DEFINES ===============================*/

#define MESSAGE_OFFSET 3
#define SERVO_OFFSET 4
#define NUM_OF_SERVOS 4

// Define the digital pins for controlling
const int enableServoPins[] = {3, 5, 6, 9};
const int pwmBuzzerPin = 8; // PWM buzzer control pin

char previousMessage[9] = ""; //Previous message

Servo servoSignal[NUM_OF_SERVOS]; //Array of servo controllers

/*============================== FUNCTIONS ==============================*/

/**
 * family_buzzer_writing(void)
 * ----------------------------
 * Controls the buzzer for the family song tune
 * 
 * Arguments:
 *        None
 *
 * Returns:
 *        N/A
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

/**
 * buzzer_writing(int number)
 * ----------------------------
 * Controls the buzzer for the family song tune
 * 
 * Arguments:
 *        number - The user to access for the buzzer tune
 *
 * Returns:
 *        N/A
**/
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

/**
 * servo_write_cycle(char* message)
 * ----------------------------
 * Checks the message from the serial port and makes alterations to 
 * servos as required
 * 
 * Arguments:
 *        message - The message received from the serial port connection
 *
 * Returns:
 *        N/A
**/
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

/**
 * servo_write_reset(void)
 * ----------------------------
 * Writes all servos to default state
 * 
 * Arguments:
 *        N/A
 *
 * Returns:
 *        N/A
**/
void servo_write_reset(void) {
  // Iterate over all servos
  for (int i = 0; i < NUM_OF_SERVOS; i++) {
    int newPosition = 0;
    if (newPosition != servoSignal[i].read()) { // Check if servo is already not in default state
      servoSignal[i].write(newPosition); // Write to servo
    }
  }
}

/**
 * setup()
 * ----------------------------
 * Default setup processes for start up of device
 * 
 * Arguments:
 *        N/A
 *
 * Returns:
 *        N/A
**/
void setup() {
  // Initialize serial communication
  Serial.begin(9600);

  for(int n = 0; n < NUM_OF_SERVOS; n++) {
    servoSignal[n].attach(enableServoPins[n]);
    servoSignal[n].write(180);
  }

  pinMode(pwmBuzzerPin, OUTPUT);
}

/**
 * loop()
 * ----------------------------
 * Main looping process of code functionality
 * 
 * Arguments:
 *        N/A
 *
 * Returns:
 *        N/A
**/
void loop() {
  if (Serial.available() >= 8) { // Check if there are at least 8 characters available in the serial buffer
    char currentMessage[9]; // Buffer to store the received message
    Serial.readBytes(currentMessage, 8); // Read the message into the buffer
    currentMessage[8] = '\0'; // Null-terminate the string

    if (strncmp(currentMessage, previousMessage, 8) != 0) {
      if ((currentMessage[MESSAGE_OFFSET] == '1')) {
        if((currentMessage[MESSAGE_OFFSET] != previousMessage[MESSAGE_OFFSET])) { //Check that previous message was also not a family event
          servo_write_reset(); // Reset the servos to default
          family_buzzer_writing(); // Start family buzzer event
        }
        delay(1000);
      } else {
        servo_write_cycle(currentMessage); //Write servos
        delay(1000);
      }
      strncpy(previousMessage, currentMessage, 8); // Copy current message to previous message
    }

  }
}