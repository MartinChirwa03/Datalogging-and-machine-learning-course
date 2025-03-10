import time
import board
import analogio

# Define the ADC pin (change this according to your board)
analog_in = analogio.AnalogIn(board.GP26)  # Replace A1 with the correct pin

def get_voltage(pin):
    """Convert raw ADC value to voltage."""
    return (pin.value * 3.3) / 65535  # Assuming 3.3V reference, 16-bit ADC

while True:
    raw_value = analog_in.value  # 16-bit ADC value (0-65535)
    voltage = get_voltage(analog_in)  # Convert to voltage
    
    print(f"Raw Value: {raw_value}, Voltage: {voltage:.2f}V")
    
    time.sleep(0.5)  # Wait before reading again
