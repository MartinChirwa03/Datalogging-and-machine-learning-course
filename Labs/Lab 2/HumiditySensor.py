import time
import board
import adafruit_dht

# Define the DHT11 pin (change D2 to your pin)
dht_pin = board.D2
dht = adafruit_dht.DHT11(dht_pin)

while True:
    try:
        # Read temperature and humidity
        temperature = dht.temperature  # °C
        humidity = dht.humidity  # %
        
        if temperature is not None and humidity is not None:
            print(f"Temp: {temperature:.1f}°C  Humidity: {humidity:.1f}%")
        else:
            print("Failed to read sensor")

    except RuntimeError as e:
        print(f"Error reading DHT11: {e}")
    
    time.sleep(2)  # DHT11 requires a delay between readings
