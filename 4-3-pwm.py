import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)


dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(15, GPIO.OUT)
GPIO.setup(dac, GPIO.OUT)
pwm = GPIO.PWM(15, 1000)
pwm.start(0)
# GPIO.output(dac, 1)
try:
    while True:
        dc = int(input('Enter new duty cycle: '))
        pwm.ChangeDutyCycle(dc)
        print(f'Expected voltage: {dc / 100 * 3.3} V')
finally:
    pwm.stop()
    GPIO.output(15, 0)
    GPIO.cleanup()
