import RPi.GPIO as GPIO
from time import sleep
from math import ceil

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17


GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=1)
GPIO.setup(comp, GPIO.IN)

def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc():
    array = [0]*8
    dec = 0
    for i in range(8):
        array[i] = 1
        GPIO.output(dac, array)
        sleep(0.01)
        c = GPIO.input(comp)
        if c == 0:
            array[i] = 0
        dec+= array[i]*2**(7-i)
    return dec

try:
    while True:
        value = adc()
        volt = 3.3 / 256 * value
        print('{:.2f}'.format(volt), 'V', value)
        forleds = ceil(value / 32)
        forleds = 2**forleds - 1
        forleds = dec2bin(forleds)
        GPIO.output(leds, forleds)
   
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()