import board
import digitalio
import time

led = digitalio.DigitalInOut(board.GP0)
button = digitalio.DigitalInOut(board.GP2)

led.direction = digitalio.Direction.OUTPUT
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

toggle=True

while True:
    led.value=toggle
    if button.value==0:
        toggle=not toggle
    time.sleep(0.1)
