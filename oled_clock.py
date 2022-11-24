import time
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
#vars
count_max_val=1000
i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)
oled.init_display()
sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)
count =count_max_val
while True:
    oled.fill(0)
    [year,month,day, hr, mi, sec,misec,micsec]= time.localtime()
    if(count ==0 or count==count_max_val):
        reading = sensor_temp.read_u16() * conversion_factor 
        temperature = 27 - (reading - 0.706)/0.001721
        temperature = round(((temperature*9)/5)+32)
        count=100
    if(month <10):
        month="0"+str(month)
    if(mi<10):
        mi="0"+str(mi)
    if(sec <10):
        sec="0"+str(sec)
    
    oled.text("Akshit's rpi", 0, 0)
    oled.text("pico Clock", 0, 8)
    oled.text(str(hr),10,20,)
    oled.text(":"+str(mi),25,20)
    oled.text(":"+str(sec),50,20)
    oled.text(str(month),10,40,)
    oled.text("/"+str(day),25,40)
    oled.text("/"+str(year),50,40)
    oled.text("Temp :"+str(temperature),10, 55)
    oled.show()
    count=count-1
