from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    for i in range(2):
        oneColumn("left")
        oneColumn("right")
    oneColumn("left")

def oneColumn(dir = "left"):
    if no_beepers_present():
            put_beeper()
    while front_is_clear():
        for i in range(4):
            move()
        if no_beepers_present():
            put_beeper()
    if dir == "left":
        turn_left()
    else:
        turn_right()
    if front_is_clear():
        move()
        if dir == "left":
            turn_left()
        else:
            turn_right()
    else:
        to_end_state()

def turn_right():
    for i in range(3):
        turn_left()
def to_end_state():
    for i in range(2):
        turn_left()
    while front_is_clear():
        move()
    turn_left()


if __name__ == "__main__":
    run_karel_program()
