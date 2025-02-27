# Requirements notes

*Note: Each one of these must be put in a view!!!*

## User requirements

USR1M: If a Thymio is behind another Thymio and has an higher speed and it's sufficiently close it must perform an overtake procedure.
USR2M: Ten seconds after the overtake procedure the Thymio must make a 180 degree turn
USR3M: When there is no event, the Thymio must follow the line
USR4M: If a Thymio is bumping into another Thymio going in the opposite direction, it must perform a collision resolution procedure
USR5R: The Thymio should operate in a $5m^2$
USR6M: There must be a road defined by 2 parallel black lines

## System requirements

SYS1R: The Thymio should avoid getting closer than 3cm to another Thymio
SYS2M: 2 minute after the start the Thymio must stop
SYS3M: The distance between two lines must be at least as big as the width of the Thymio
SYS4M: The width of the black lines must be in the range $[1.5cm, 2cm]$
SYS5M: The SoS must be composed of 2 Thymio robots
SYS6M: The Thymio must be placed on the same line one in front of the other at the start
SYS7O: The road may be circular
SYS8M: The road must not include any obstacle

IMP1M: The Thymio must register the power of each motor
IMP2R: The Thymio should keep the speed between $[0.5m/s, 1m/s]$

## Communication/RUI

### CS-level

SYS9M: The Thymio must include 5 infrared sensors in the front  
SYS10M: The Thymio must include 1 infrared sensor in the bottom to detect the black lines
SYS11O: The Thymio may include 2 or more infrared sensors in the rear
IMP3M: The Thymio must provide a wired programming interface
IMP4R: The Thymio should provide a wireless programming interface
IMP5R: The Thymio should have at least 1 led for each side to warn the user about it's state
IMP6R: The Thymio should have a buzzer to warn the user about it's state

### SoS-level

SYS12M: The Thymio must be able to understand if it's going faster than then Thymio in front of it by realizing that it's getting closer to it as time goes using the infrared sensors in the front
