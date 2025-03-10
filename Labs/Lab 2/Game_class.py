import board
import digitalio
import time
import random

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
points=0
while True:
    print("Points",points)
    ... #randomly generate a sequence
    ... #play sequence
    #wait for response
    response=False
    user_sequence=[]
    while not response:
        pressed=getButtons()#get the buttons
        ... #gather each button in the user sequence
        #check that the button pressed is the next one in the sequence
        if ...: #if button is pressed
            if ....: # if the button is wrong
                print("Incorrect")
                response=True
            elif ...: #it is correct and sequence is of the same length
                print("Correct, generating new")
                response=True
                points+=1
                