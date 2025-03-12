import board
import busio
import sdcardio
import storage
import os
import time
from sensors import *

#initialise the spi
spi = busio.SPI(clock=board.GP2,MOSI=board.GP3,MISO=board.GP4)
cs = board.GP16

#sd card init
sdcard = sdcardio.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")
print("successful mount")

def is_space():
    #output memory usage
    stats = vfs.statvfs("/sd")
    total_space=stats[2]*stats[1]
    free_space = stats[3] * stats[1]
    used_space = total_space-free_space
    if used_space/(1024**3)<14: #space exists
        return 1
    return 0


# Test writing to a file
with open("/sd/test.csv", "w") as file:
    l = light(board.GP27) # collect lab
    for i in range(1000): #loop through trial
        if is_space(): #only write if there is space
            t1=time.monotonic()
            val=l.readPin()
            file.write(str(time.monotonic()-t1)+","+str(val)+"/n")
            time.sleep(0.05)
print("File written successfully!")
