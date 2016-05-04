import RPi.GPIO as GPIO
import time
import pyautogui
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i','--gpio', help='GPIO port (BCM)',required=True)
parser.add_argument('-t','--trigger', help='Key to press',required=True)
args = parser.parse_args()

# configuration
singleclick = 1 # when sensor is activated, only press key once instead
debug = 1 # debug messages

GPIO.setmode(GPIO.BCM)
if debug == 1: print("mode: GPIO.BCM")

channel = int(args.gpio)
if debug == 1: print("channel: gpio{0:02d}".format(channel))

trigger = args.trigger

GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
if debug == 1: print("gpio{0:02d} set as GPIO.IN.".format(channel))

# keystate 0 = up, 1 = down
keystate = 0

while True:
  time.sleep(0.00001)

  if GPIO.input(channel):
    if keystate == 0:
      keystate = 1
      pyautogui.press(trigger)
  else:
    keystate = 0

    time.sleep(0.1)

