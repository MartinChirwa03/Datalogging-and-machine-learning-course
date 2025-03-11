
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

... #setup spi

... #set up record button
while True:
    #use your LED toggle code from yesterdays lab
    #when you toggle the button on, it should start recording
    #when you toggle the button off, it should stop
    #try adding an LED to show if it is recording or not
    #have the filename change everytime you start a new recording

