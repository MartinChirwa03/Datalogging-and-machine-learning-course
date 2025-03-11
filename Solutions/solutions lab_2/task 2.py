import board
import digitalio
import time

led = digitalio.DigitalInOut(board.GP0)
button = digitalio.DigitalInOut(board.GP2)

led.direction = digitalio.Direction.OUTPUT
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

while True:
    if button.value:
        led.value=1
    else:
        led.value=0
    time.sleep(0.1)
