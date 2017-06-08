import RPi.GPIO as GPIO
import time

class Lcd():
    def __init__(self,par_rs, par_rw, par_e,par_pin0,par_pin1,par_pin2,par_pin3):
        self.__rs = par_rs
        self.__rw = par_rw
        self.__e = par_e
        self.__pin0 = par_pin0
        self.__pin1 = par_pin1
        self.__pin2 = par_pin2
        self.__pin3 = par_pin3


        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.__rs, GPIO.OUT)
        GPIO.setup(self.__rw, GPIO.OUT)
        GPIO.setup(self.__e, GPIO.OUT)
        GPIO.setup(self.__pin0, GPIO.OUT)
        GPIO.setup(self.__pin1, GPIO.OUT)
        GPIO.setup(self.__pin2, GPIO.OUT)
        GPIO.setup(self.__pin3, GPIO.OUT)

    def __ehoog_instructie(self):
        GPIO.output(self.__rs, GPIO.LOW)
        GPIO.output(self.__e, GPIO.HIGH)
        GPIO.output(self.__rw, GPIO.LOW)

    def __elaag_instructie(self):
        GPIO.output(self.__rs, GPIO.LOW)
        GPIO.output(self.__e, GPIO.LOW)
        GPIO.output(self.__rw, GPIO.LOW)

    def __ehoog_data(self):
        GPIO.output(self.__rs, GPIO.HIGH)
        GPIO.output(self.__e, GPIO.HIGH)
        GPIO.output(self.__rw, GPIO.LOW)

    def __elaag_data(self):
        GPIO.output(self.__rs, GPIO.HIGH)
        GPIO.output(self.__e, GPIO.LOW)
        GPIO.output(self.__rw, GPIO.LOW)

    def __set_GPIO_data_bits(self,data):
        filter = 0x08
        list = []
        for i in range(0, 4):
            bit = data & filter
            filter = filter >> 1
            if (bit == 0):
                list.append(bit)
            else:
                list.append(1)

        self.__ehoog_data()
        GPIO.output(self.__pin3, list[0])
        GPIO.output(self.__pin2, list[1])
        GPIO.output(self.__pin1, list[2])
        GPIO.output(self.__pin0, list[3])
        self.__elaag_data()
        time.sleep(0.00004)

    def __set_GPIO_instruction_bits(self, data, delay):
        filter = 0x08
        list = []
        for i in range(0, 4):
            bit = data & filter
            filter = filter >> 1
            if (bit == 0):
                list.append(bit)
            else:
                list.append(1)

        self.__ehoog_instructie()
        GPIO.output(self.__pin3, list[0])
        GPIO.output(self.__pin2, list[1])
        GPIO.output(self.__pin1, list[2])
        GPIO.output(self.__pin0, list[3])
        self.__elaag_instructie()
        time.sleep(delay)

    def __function_reset(self):
        time.sleep(0.015)
        self.__set_GPIO_instruction_bits(0x03, 0.0040)
        self.__set_GPIO_instruction_bits(0x03, 0.0001)
        self.__set_GPIO_instruction_bits(0x03, 0.0040)
        self.__set_GPIO_instruction_bits(0x02, 0.0040)

    def __function_set(self):
        self.__set_GPIO_instruction_bits(0x28 >> 4,0.00004)
        self.__set_GPIO_instruction_bits(0x28, 0.00004)

    def __function_on(self):
        self.__set_GPIO_instruction_bits(0x0f >> 4,0.00004)
        self.__set_GPIO_instruction_bits(0x0f, 0.00004)

    def __function_clear(self):
        self.__set_GPIO_instruction_bits(0x01 >> 4, 0.001)
        self.__set_GPIO_instruction_bits(0x01, 0.00164)

    @staticmethod
    def function_clear(self):
        self.__set_GPIO_instruction_bits(0x01 >> 4, 0.001)
        self.__set_GPIO_instruction_bits(0x01, 0.00164)
    @staticmethod
    def function_cursor(self, data):
        self.__set_GPIO_instruction_bits(data >> 4, 0.00004)
        self.__set_GPIO_instruction_bits(data, 0.00004)


    def __data_write_char(self, character):
        self.__set_GPIO_data_bits(ord(character) >> 4)
        self.__set_GPIO_data_bits(ord(character))

    @staticmethod
    def function_init(self):
        self.__function_reset()
        self.__function_set()
        self.__function_on()
        self.__function_clear()



    @staticmethod
    def function_print(self, zin):
        if (len(zin) > 32):
            zin = "te veel characters"
            zin_lijst = list(zin)
            for item in zin_lijst:
                self.__data_write_char(item)
        else:
            zin_lijst = list(zin)
            for item in zin_lijst:
                self.__data_write_char(item)