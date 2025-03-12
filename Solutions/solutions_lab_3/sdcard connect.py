import board
import busio
import sdcardio
import storage
import os

#initialise the spi
spi = busio.SPI(clock=board.GP2,MOSI=board.GP3,MISO=board.GP4)
cs = board.GP16

#sd card init
sdcard = sdcardio.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")
print("successful mount")

#output memory usage
stats = vfs.statvfs("/sd")
total_space=stats[2]*stats[1]
free_space = stats[3] * stats[1]
used_space = total_space-free_space

print(used_space/(1024*1024),"MB")


print("SD card mounted successfully!")

# Test writing to a file
with open("/sd/test.txt", "w") as file:
    file.write("Hello, SD card!\n")

print("File written successfully!")
