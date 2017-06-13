#imports
from model.Lcd import Lcd
from model.DbClass import DbClass
import RPi.GPIO as GPIO
import datetime
import math


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
hallsensor = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(hallsensor, GPIO.IN)

#setup lcd--------------------------------------------------------------------
lcdtest = Lcd(26, 5, 6, 22, 24, 19, 25)
Lcd.function_init(lcdtest)

#setup db
getdatum = DbClass()
getinfo = DbClass()
newday = DbClass()

#enable event-----------------------------------------------------------------
GPIO.add_event_detect(18, GPIO.BOTH)

#variables--------------------------------------------------------------------
previous_time = time_to_seconds(datetime.datetime.now())
radius = 35
lengt_weel = radius *2 * math.pi
lengt_half_weel = lengt_weel/2
isuploaded = True

#database variables
date = str(datetime.datetime.now()).split(' ')[0]
average_speed = 0
if(not getdatum.getcollection(date)):
    total_distence = 0
    driven_time = 0
    pauzed_time = 0
    newday.make_new_day(date,total_distence,driven_time,pauzed_time,str(average_speed)+"km")
else:
    data = getinfo.getcollection(date)
    total_distence = data[3]
    driven_time = data[4]
    pauzed_time = data[5]

print(total_distence)
#loop-------------------------------------------------------------------------
while True:
    hall = GPIO.input(hallsensor)
    if GPIO.event_detected(18):
        Lcd.function_clear(lcdtest)
        #total distence
        total_distence += lengt_half_weel
        #time driven and pauzed
        time_now = time_to_seconds(datetime.datetime.now())
        timedifrence = time_now - previous_time
        if (timedifrence >= 30):
            pauzed_time += timedifrence
        else:
            driven_time += timedifrence
        #save new time
        previous_time = time_now
        #print on lcd
        speed = lengt_half_weel / timedifrence / 100000 * 3600
        Lcd.function_print(lcdtest, str(speed))
        isuploaded = False

    if(isuploaded):
        average_speed = total_distence / driven_time / 100000 * 3600
        isuploaded = True





