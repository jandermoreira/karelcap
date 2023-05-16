"""
Novo Karel
"""
from KarelCAP import *

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def main():
    """"""
    turn_left()
    for i in range(4):
        while front_is_clear():
            move()
        turn_right()
        put_beeper()


Execute()
