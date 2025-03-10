import time
import board
import digitalio

# Define button pin
button = digitalio.DigitalInOut(board.D3)  # Change to your pin
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP  # Enable internal pull-up resistor

while True:
    if not button.value:  # Button pressed (LOW)
        print("Button Pressed!")
    else:
        print("Button Released!")

    time.sleep(0.1)  # Short delay to avoid spamming output
