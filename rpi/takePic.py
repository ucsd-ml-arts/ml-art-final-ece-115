#import necessary libraries
import RPi.GPIO as GPIO
from gpiozero import Button, LED
from picamera import PiCamera
from datetime import datetime
from time import sleep
import subprocess
import sys

#function when button is pressed
def capture():
    print('Captured')
    timestamp = datetime.now().isoformat()
    img = '../samples_content/%s.jpg' % timestamp
    camera.capture(img)
    camera.stop_preview()
    subprocess.Popen(['xdg-open',img])
    sleep(7)
    camera.start_preview()

#defining GPIO pins
led = LED(2)
take_pic_btn = Button(4)

#initializing camera object
camera = PiCamera()
#camera.resolution = (500,500)
camera.start_preview()
print('Take a picture!')

while(True):
    #call LED and button functions
    try:
        led.source = take_pic_btn
        take_pic_btn.when_released = capture
    #exit camera and clean GPIO on keyboard interrupt
    except KeyboardInterrupt:
        print('Interrupted')
        GPIO.cleanup()
        camera.stop_preview()
        camera.close()
        sys.exit(0)