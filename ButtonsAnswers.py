import RPi.GPIO as GPIO
import time
import sys
sys.path.append("/home/pi/Downloads/PyAutoGUI-0.9.33")
import pyautogui

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

time.sleep(0.2)

while True:
    button_1 = GPIO.input(18)
    button_2 = GPIO.input(4)

    if button_2 == False:
        print('Yellow Button No')
        pyautogui.press("0")
    
    if button_1 == False:
        print('Blue Button Yes')
        pyautogui.press("1")

    time.sleep(0.2)
