import datetime
from model.Lcd import Lcd

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

lcdtest = Lcd(26, 5, 6, 22, 24, 19, 25)
Lcd.function_init(lcdtest)

while True:
    isgo = input("type go om tijd in seconden te krijgen")
    Lcd.function_clear(lcdtest)
    if (isgo == "go"):
        Lcd.function_print(lcdtest, str(time_to_seconds(datetime.datetime.now())))
    else:
        Lcd.function_print(lcdtest, "only go works")
