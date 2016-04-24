import RPi.GPIO as GPIO
import time
import sys
sys.path.append("/home/pi/Downloads/PyAutoGUI-0.9.33")
import pyautogui
GPIO.setmode(GPIO.BCM)

TRIG = 23 
ECHO = 24

FLAG = True

print "Distance Measurement In Progress"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)

while True:
  GPIO.output(TRIG, True)


  time.sleep(0.00001)
  GPIO.output(TRIG, False)

  while GPIO.input(ECHO)==0:
    pulse_start = time.time()

  while GPIO.input(ECHO)==1:
    pulse_end = time.time()

  pulse_duration = pulse_end - pulse_start

  distance = pulse_duration * 17150

  distance = round(distance, 2)

  print "Distance:",distance,"cm"

  if distance <= 60 and FLAG is True:
    FLAG = False
    print "Less than 60"
    pyautogui.press("enter")

  if distance >= 70 and FLAG is False:
    FLAG = True
    print "More than 60"    
  
  time.sleep(0.2)


