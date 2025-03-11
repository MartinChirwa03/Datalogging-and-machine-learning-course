
class datalogger:
    def __init__(self,SPI):
        ...
        #set up sd and file
    def create_file(self,name):
        ....
    def write_data(self,data):
        ...
        #if there is space
        #write data in the chosen format
    def isSpace(self):
        ...
        #check how much space there is
    def close(self):
        ...
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

