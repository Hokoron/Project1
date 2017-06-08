from model.Lcd import Lcd
import RPi.GPIO as GPIO
import time

hallsensor = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(hallsensor, GPIO.IN)

print("program running!")

lcdtest = Lcd(26, 5, 6, 22, 24, 19, 25)
Lcd.function_init(lcdtest)

while True:
    hall = GPIO.input(hallsensor)
    Lcd.function_clear(lcdtest)
    if (hall == 0):
        Lcd.function_print(lcdtest, "aan" )
    else:
        Lcd.function_print(lcdtest, "uit")
    time.sleep(1)



