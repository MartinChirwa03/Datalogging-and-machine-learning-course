import digitalio
import board
import busio
import sdcardio
import storage
import os
import time
from sensors import *

class datalogger:
    def __init__(self,SPI,cs):
        sdcard = sdcardio.SDCard(spi, cs)
        self.vfs = storage.VfsFat(sdcard)
        storage.mount(self.vfs, "/sd")
        print("successful mount")
        #set up sd and file
    def create_file(self,filename):
        self.file=open("/sd/"+filename,"w")
    def write_data(self,data):
        if self.isSpace():
            try:
                self.file.write(data)
            except:
                print("Could not write") #you could also consider putting errors or LED flashes here
        #if there is space
        #write data in the chosen format
    def isSpace(self):
        stats = self.vfs.statvfs("/sd")
        total_space=stats[2]*stats[1]
        free_space = stats[3] * stats[1]
        used_space = total_space-free_space
        if used_space/(1024**3)<14: #space exists
            return 1
        return 0
        #check how much space there is
    def close(self):
        self.file.close()
        #close and save the file

#main control
if __name__ == "__main__":
    #setup spi
    spi = busio.SPI(clock=board.GP2,MOSI=board.GP3,MISO=board.GP4)
    cs = board.GP16
    data=datalogger(spi,cs)

    #set up record button
    led = digitalio.DigitalInOut(board.GP1)
    button = digitalio.DigitalInOut(board.GP0)

    led.direction = digitalio.Direction.OUTPUT
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP

    filename="mydata"
    toggle=False
    recordings=0

    l = light(board.GP27) # collect light
    h = humidity(board.GP17)

    while True: #use your LED toggle code from yesterdays lab
        led.value=toggle
        if button.value==0: #when you toggle the button on, it should start recording
            toggle=not toggle
            if toggle: #have the filename change everytime you start a new recording
                f=filename+str(recordings)+".csv"
                data.create_file(f) 
                data.write_data("time,light,humidity,temperature\n") #make keys
            else: #when you toggle the button off, it should stop
                try:
                    data.close()
                    recordings+=1
                    print("file saves...")
                except:
                    pass
            time.sleep(0.5)
        led.value=toggle #try adding an LED to show if it is recording or not
        if toggle: #if recording gather all the sensors
            t1=time.monotonic()
            light_reading=l.readPin()
            humid=h.getHumidity()
            temp=h.getTemp()
            data.write_data(str(time.monotonic()-t1)+","+str(light_reading)+","+str(humid)+","+str(temp)+"\n")
            print(str(time.monotonic()-t1)+","+str(light_reading)+","+str(humid)+","+str(temp))
            
        time.sleep(0.1)