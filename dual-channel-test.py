import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
L_CHANNEL = 17
R_CHANNEL = 18

GPIO.setup(L_CHANNEL, GPIO.IN)
GPIO.setup(R_CHANNEL, GPIO.IN)
print("")
print("")
print("        | L |         | R |")

while True:
  time.sleep(0.00001)

  if GPIO.input(L_CHANNEL):
    print("        | # |", end="")
  else:
    print("        |   |", end="")

  if GPIO.input(R_CHANNEL):
    print("         | # |", end="\r")
  else:
    print("         |   |", end="\r")

    time.sleep(0.2)

