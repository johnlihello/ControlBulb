import RPi.GPIO as GPIO
import time

LED_PIN = 3
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)

GPIO.output(LED_PIN, 1)

print("hello")
GPIO.cleanup()