import RPi.GPIO as GPIO
import time

GPIO.cleanup()
LED_PIN = 3
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)

GPIO.output(LED_PIN, 1)
GPIO.setwarnings(False)
GPIO.cleanup()
