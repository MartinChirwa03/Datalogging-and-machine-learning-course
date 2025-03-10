from karel.stanfordkarel import * 

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should leave
a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    len = count_length()
    turn_around()
    move_forward(int(len/2))
    put_beeper()

def count_length():
    length = 0
    while front_is_clear():
        move()
        length += 1
    return length

def turn_around():
    for i in range(2):
        turn_left()

def move_forward(step_length=1):
    for i in range(step_length):
        move()



if __name__ == "__main__":
    run_karel_program()
