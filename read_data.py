from machine import ADC
import time

adc = ADC(Pin(26))  # Assuming the sensor is connected to ADC_0 (GP26)

def read_pulse():
    value = adc.read_u16()
    return value

while True:
    pulse_value = read_pulse()
    print(pulse_value)
    time.sleep(0.1)