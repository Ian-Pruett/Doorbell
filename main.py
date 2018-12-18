from machine import Pin
import time


# read wifi connection password stored locally
def read_file(filename):
    import uio
    file = uio.open(filename, 'r')
    lines = file.readlines()
    file.close()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n', '')
    return lines


# method to connect to wifi network
def do_connect(ssid, password):
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    print('SUCCESS, network config:', sta_if.ifconfig())