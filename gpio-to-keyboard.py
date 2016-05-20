"""
gpio-to-keyboard: Convert Raspberry GPIO state changes into keyboard events.

TODO:
  * --hold option. When on, ignores RELEASE and bind
    sensor on/off to events key down/up respectively.
  * --board option for GPIO.BOARD support
  * --interval option to change the loop interval
  * --lazy-delay --lazy-interval: after LAZY-DELAY time of inactivity,
    enters in lazy mode, looping every LAZY-INTERVAL only to reduce
    CPU activity
  * --config option to support input file with list of multiple bindings
  * create a script from this one called gpio-run to automate scripts
    instead of emulating keyboard.

 To install dependencies:
   pip install pyautogui
   pip install argparse

Author: Paulo Amaral
"""

import RPi.GPIO as GPIO
import time
import pyautogui
import argparse

parser = argparse.ArgumentParser(description="Convert Raspberry GPIO state changes into keyboard events.\nrequires: pyautogui, argparse, run in a X session, root (use sudo)")
parser.add_argument('-i','--gpio', help='GPIO port (BCM)',required=True)
parser.add_argument('-e','--enter', help='Key to press when sensor activates (e.g. A B 1 2 space tab enter)',required=False)
parser.add_argument('-l','--leave', help='Key to press when sensor deactivates (e.g. A B 1 2 space tab enter)',required=False)
parser.add_argument('-v','--verbose', help='Show debug messages', required=False, action='store_true')
parser.add_argument('-0','--inverse', help='For sensors where enter=0V (low) and leave=3V (high)',required=False, action='store_true')
args = parser.parse_args()

# debug messages
debug = args.verbose

GPIO.setmode(GPIO.BCM)
if debug: print("mode: GPIO.BCM")

channel = int(args.gpio)
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
if debug: print("channel: gpio_{0:02d} (input)".format(channel))

enter = args.enter
if debug: print("enter: {0}".format(enter))

leave = args.leave
if debug: print("leave: {0}".format(leave))

# keystate 0 = up, 1 = down
keystate = 0

if (args.inverse):
  sensor_out = True
  sensor_in = False
else:
  sensor_out = False
  sensor_in = True

while True:
  time.sleep(0.00001)

  if GPIO.input(channel) == sensor_in:
    if keystate == 0:
      keystate = 1 
      if enter is not None: pyautogui.press(enter)
  else:
    if keystate == 1:
      keystate = 0
      if leave is not None: pyautogui.press(leave)

    time.sleep(0.1)

