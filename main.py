from machine import Pin
import time

led = Pin(2, Pin.OUT)  # Change pin based on your board

while True:
    led.value(1)  # LED ON
    time.sleep(1)
    led.value(0)  # LED OFF
    time.sleep(1)
