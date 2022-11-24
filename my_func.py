import machine
import time
from secrets import secrets
#Functions
# Define blinking function for onboard LED to indicate error codes
def blink_onboard_led(num_blinks):
    led = machine.Pin('LED', machine.Pin.OUT)
    for i in range(num_blinks):
        led.on()
        time.sleep(.2)
        led.off()
        time.sleep(.2)

#function to connect to wlan
def connect_wlan(wlan):
    # Load login data from different file for safety reasons
    ssid = secrets['ssid']
    pw = secrets['pw']
    wlan.connect(ssid, pw)
    # Wait for connection with 10 second timeout
    timeout = 10
    while timeout > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            print('Status=',wlan.status())
            break
        timeout -= 1
        print('Waiting for connection...')
        time.sleep(1)    
    # Handle connection error
    # Error meanings
    # 0  Link Down
    # 1  Link Join
    # 2  Link NoIp
    # 3  Link Up
    # -1 Link Fail
    # -2 Link NoNet
    # -3 Link BadAuth
    blink_onboard_led(wlan.status())
    if wlan.status() != 3:
        raise RuntimeError('Wi-Fi connection failed')
    else:
        print('Connected')
        status = wlan.ifconfig()
        print('ip = ' + status[0])
        
# Function to load in html page    
def get_html(html_name):
    with open(html_name, 'r') as file:
        html = file.read()
        
    return html