from machine import Pin

rot_a = Pin(14, Pin.IN, Pin.PULL_UP)
rot_b = Pin(15, Pin.IN, Pin.PULL_UP)
rot_switch = Pin(16, Pin.IN, Pin.PULL_UP)

def rotary_callback(pin):
    if rot_a.value() == rot_b.value():
        print("Clockwise")
    else:
        print("Counter-Clockwise")

rot_a.irq(trigger=Pin.IRQ_RISING, handler=rotary_callback)