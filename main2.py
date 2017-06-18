#imports
from model.Lcd import Lcd
import RPi.GPIO as GPIO
from model.dbClass import dbClass
import datetime
import math
import time


#functions------------------------------------------------------------------------
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

#setup------------------------------------------------------------------------
hallsensor = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(hallsensor, GPIO.IN)

#setup db
getdatum = dbClass()
getinfo = dbClass()
newday = dbClass()
update = dbClass()

#setup lcd--------------------------------------------------------------------
lcdtest = Lcd(21, 20, 16, 25, 24, 23, 18)
Lcd.function_init(lcdtest)

#enable event-----------------------------------------------------------------
GPIO.add_event_detect(hallsensor, GPIO.BOTH)

#variables--------------------------------------------------------------------
previous_time = time_to_seconds(datetime.datetime.now())
previous_time2 = time_to_seconds(datetime.datetime.now())
radius = 36
lengt_weel = radius *2 * math.pi
lengt_half_weel = lengt_weel/2
isuploaded = True
isstart = True
speed = []

#database variables
date = str(datetime.datetime.now()).split(' ')[0]
average_speed = 0
total_distence = 0
driven_time = 0
pauzed_time = 0
if(not getdatum.getcollection(date)):
    newday.make_new_day(date,total_distence,driven_time,pauzed_time,average_speed)
else:
    save =  getinfo.getcollection(date)
    total_distence = save[2]
    driven_time = save[3]
    pauzed_time = save[4]
    average_speed =save[5]

#loop-------------------------------------------------------------------------
while True:
    if GPIO.event_detected(hallsensor):
        if(isstart):
            previous_time = time_to_seconds(datetime.datetime.now())
        # total distence
        total_distence += lengt_half_weel/100
        # time driven and pauzed
        time_now = time_to_seconds(datetime.datetime.now())
        timedifrence = time_now - previous_time
        if (timedifrence >= 5):
            pauzed_time += timedifrence
        else:
            driven_time += timedifrence
        # save new time
        previous_time = time_now#
        if(not isstart):
            speed.append(lengt_half_weel / timedifrence / 100000 * 3600)
        isuploaded = False
        average_speed = total_distence / driven_time / 1000 * 3600
        isstart = False

    # print on lcd
    time_now2 = time_to_seconds(datetime.datetime.now())
    timedifrence2 = time_now2 - previous_time2
    if (timedifrence2 >= 1):
        Lcd.function_clear(lcdtest)
        prined_speed =0
        count = 0
        for items in speed:
            prined_speed += items
            count += 1
        try:
            prined_speed = prined_speed / count
        except:
            prined_speed = 0
        prined_speed = round(prined_speed,1)
        Lcd.function_print(lcdtest, str(prined_speed))
        Lcd.function_print(lcdtest, " Km")
        previous_time2 = time_now2
        speed = []

    if(not isuploaded):
        isuploaded = True
        average_speed = total_distence / driven_time / 1000 * 3600
        update.updatekilometer(date,total_distence,driven_time,pauzed_time,average_speed)
