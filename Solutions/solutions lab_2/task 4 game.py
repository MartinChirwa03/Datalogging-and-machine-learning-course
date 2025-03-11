"""
Disclaimer, this code uses a different method to the demo code

"""
import board
import digitalio
import time
import random

#initialise the LEDs
led1 = digitalio.DigitalInOut(board.GP17)
led2 = digitalio.DigitalInOut(board.GP18)
led3 = digitalio.DigitalInOut(board.GP20)

led1.direction = digitalio.Direction.OUTPUT
led2.direction = digitalio.Direction.OUTPUT
led3.direction = digitalio.Direction.OUTPUT

#initialise the buttons
button1 = digitalio.DigitalInOut(board.GP0)
button2 = digitalio.DigitalInOut(board.GP1)
button3 = digitalio.DigitalInOut(board.GP2)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.UP
button3.direction = digitalio.Direction.INPUT
button3.pull = digitalio.Pull.UP

#place into neat arrays
LEDS=[led1,led2,led3]
buttons=[button1,button2,button3]

def get_sequence(length): #make a squence
    sequence=[]
    for j in range(length):
        sequence.append(random.choice([i for i in range(len(buttons))])) #pick the indices of the buttons
    return sequence

def get_buttons():
   return [not button.value for button in buttons]

def play_sequence(seq):
    for num in seq:
        LEDS[num].value=True
        time.sleep(0.5)
        LEDS[num].value=False
        time.sleep(0.5)

def check_answer(sequence,user):
    correct=0
    for i in range(len(sequence)):
        if sequence[i]==user[i]:
            correct+=1
    return correct==len(sequence)

resting_state=get_buttons()
points=0
round_=1
waiting=False
record=[]
sequence=[]
while True:
    pressed=get_buttons()
    if not waiting: #play the sequence
        sequence=get_sequence(round_)
        play_sequence(sequence)
        waiting=True
        print("your turn... sequence size",round_)
    else:
        if sum(resting_state)!=sum(pressed): #if pressed
            ind=0
            if pressed[0]: ind=0
            elif pressed[1]: ind=1
            elif pressed[2]: ind=2
            record.append(ind)
            time.sleep(0.5) #give time to get finger off the button
            
        if len(record)==len(sequence):#check once the code is done
            result=check_answer(sequence,record)
            sequence=[]
            record=[]
            if result:
                points+=1
                print("Well done... current points are on",points,"The challenge will now get harder")
                round_+=1
                waiting=False
            else:
                print("You lose!!! Restarting")
                round_=1
                points=0
                waiting=False
                
    time.sleep(0.1)
