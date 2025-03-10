from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""


def main():
    move_to_newspaper()
    pick_up_newspaper()
    return_to_start()

def move_to_newspaper():
    move_forward(2)
    turn_right()
    move_forward(1)
    turn_left()
    move_forward(1)

def move_till_stop():
    while front_is_clear():
        move()

def move_forward(step_length=2):
    for i in range(step_length):
        move()

def pick_up_newspaper():
    pick_beeper()

def return_to_start():
    turn_around()
    move_till_stop()
    turn_right()
    move()
    turn_right()

def turn_around():
    for i in range(2):
        turn_left()

def turn_right():
    for i in range(3):
        turn_left()


if __name__ == "__main__":
    run_karel_program()
