import esp
esp.osdebug(None)

import gc
#import webrepl
#webrepl.start()
gc.collect()

# set overclock to speed up timing issues with irsend
import machine
machine.freq(160000000)

'''MAIN PROGRAM'''
from main import *

credentials = read_file('credentials.txt')

@micropython.native
def btn_led_event(p):
    import urequests as requests
    import ujson as json
    data = {'BotEmail': credentials[1], 'BotPassword':credentials[2]}
    D1.on()
    r = requests.post(credentials[0], data=json.dumps(data), headers={'Content-Type': 'application/json'})
    time.sleep(1)
    D1.off()

# establish connection
info = read_file('wifi_info.txt')
do_connect(info[0], info[1])


D1 = Pin(5, Pin.OUT)
D2 = Pin(4, Pin.IN)

D2.irq(trigger=Pin.IRQ_FALLING, handler=btn_led_event)