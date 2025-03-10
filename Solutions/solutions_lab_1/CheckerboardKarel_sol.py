from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    direction = True
    while front_is_clear():
        row(direction)
        move_next(direction)
        direction = not direction

def row(direction):
    pattern2()
    while front_is_clear():
        move()
        pattern2()
    if direction:
        turn_left()
    else:
        for i in range(3): 
            turn_left()

def move_next(direction):
    if front_is_clear():
        move()
        if direction:
            turn_left()
        else:
            for i in range(3):
                turn_left()

def pattern2():
    put_beeper()
    move()

if __name__ == "__main__":
    run_karel_program()
