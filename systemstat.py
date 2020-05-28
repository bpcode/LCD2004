import I2C_LCD_driver
import socket
import fcntl
import struct
import psutil
import time

mylcd = I2C_LCD_driver.lcd()

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,
        struct.pack('256s', ifname[:15])
    )[20:24])

ipAdd = get_ip_address('wlan0')


while True:
    cpuUt = int(round(psutil.cpu_percent(),0))
    ramUt = int(round(psutil.virtual_memory().percent,0))
    cpuT = int(round(psutil.sensors_temperatures()['cpu-thermal'][0].current,0))
    diskU = int(round(psutil.disk_usage('/').percent,0))
    mylcd.lcd_display_string("CPU: "+ str(cpuUt) +"%", 1,0)
    mylcd.lcd_display_string("RAM: "+ str(ramUt)+"%", 1,10)
    mylcd.lcd_display_string("CPU Temp: "+ str(cpuT)+chr(223)+"C", 3)
    mylcd.lcd_display_string("Disk Used: "+ str(diskU)+"%", 4)
    time.sleep(5)
    mylcd.lcd_clear()
