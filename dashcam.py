import datetime  
import picamera  
import re
import RPi.GPIO as GPIO  
import time
import sys
from screeninfo import get_monitors

# get the current screen res

resolution = re.search(r'(\d{3,4})x(\d{3,4})', str(get_monitors()[0]))
res_x = int(resolution.group(1))
res_y = int(resolution.group(2))

app_screen_space = res_x * 0.15
res_x = res_x - int(app_screen_space)
#print(get_monitors()[0], res_x)

#GPIO.setmode(GPIO.BCM)  
#GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)  

while True:  
    #GPIO.wait_for_edge(24, GPIO.FALLING)  
    vid_name = datetime.datetime.now().strftime("%y%m%d_%H%M%S")  
    with picamera.PiCamera() as camera:  
        camera.resolution = (res_x, res_y)  
        camera.start_preview()  
        camera.start_recording('/home/pi/' + vid_name + '.h264')  
        #GPIO.wait_for_edge(24, GPIO.RISING)  
        time.sleep(10);
        camera.stop_recording()  
        break

GPIO.cleanup()  
