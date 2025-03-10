import time
import board
import busio
import adafruit_mpu6050

# Initialize I2C bus
i2c = busio.I2C(board.SCL, board.SDA)  # Uses default I2C pins

# Initialize MPU6050
mpu = adafruit_mpu6050.MPU6050(i2c)

while True:
    # Read accelerometer data
    accel_x, accel_y, accel_z = mpu.acceleration
    
    # Read gyroscope data
    gyro_x, gyro_y, gyro_z = mpu.gyro
    
    # Read temperature
    temperature = mpu.temperature

    # Print readings
    print(f"Accel: X={accel_x:.2f} m/s², Y={accel_y:.2f} m/s², Z={accel_z:.2f} m/s²")
    print(f"Gyro: X={gyro_x:.2f}°/s, Y={gyro_y:.2f}°/s, Z={gyro_z:.2f}°/s")
    print(f"Temperature: {temperature:.2f}°C")
    print("-" * 40)

    time.sleep(0.5)  # Wait before the next reading
