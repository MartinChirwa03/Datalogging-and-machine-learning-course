import board
import digitalio
import time


led1 = ...
led2 = ...
led3 = ...

LEDS=[led1,led2,led3]

def play_sequence(seq): #take in a sequence of each index of the LED that should be selected
    for num in seq:
        LEDS[num].value=True
        time.sleep(0.5)
        LEDS[num].value=False
        time.sleep(0.5)

button1 = ...
button2 = ...
button3 = ...

buttons=[]

def getButtons():
    ...

initial_state=getButtons() #get the initial states of the buttons

while True:
    pressed=getButtons()#get the buttons
    