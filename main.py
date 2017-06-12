from model.Lcd import Lcd
import RPi.GPIO as GPIO
import datetime
import math
import time

def time_to_seconds(time):
    strdatetime = str(time)
    datetimelijst = strdatetime.split(' ')
    strtime = datetimelijst[1]
    timelijst = strtime.split(':')
    hour = float(timelijst[0])
    min = float(timelijst[1])
    sec = float(timelijst[2])
    time_in_seconds = sec + min * 60 + hour * 60 * 60
    return time_in_seconds

hallsensor = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(hallsensor, GPIO.IN)
lcdtest = Lcd(26, 5, 6, 22, 24, 19, 25)
Lcd.function_init(lcdtest)
GPIO.add_event_detect(18, GPIO.BOTH)
previous_time = time_to_seconds(datetime.datetime.now())
radius = 35
lengt_weel = radius *2 * math.pi
lengt_half_weel = lengt_weel/2

while True:
    hall = GPIO.input(hallsensor)
    if GPIO.event_detected(18):
        Lcd.function_clear(lcdtest)
        time_now = time_to_seconds(datetime.datetime.now())
        timedifrence = time_now - previous_time
        previous_time = time_now
        speed = lengt_half_weel / timedifrence / 100000 * 3600
        Lcd.function_print(lcdtest, str(speed))



