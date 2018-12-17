from machine import Pin
import time

def btn_led_event(p):
    print('value of button is ', p)
    D1.on()
    time.sleep(1)
    D1.off()

D1 = Pin(5, Pin.OUT)
D2 = Pin(4, Pin.IN)

D2.irq(trigger=Pin.IRQ_FALLING, handler=btn_led_event)