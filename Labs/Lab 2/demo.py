from sensors import *
import board

# try light sensor
l = light(board.GP27)
print("Light value=",l.readPin())

# try co2 sensor
c = co2(board.GP28)
print("CO2 value=",l.readPin())

# try sound sensor
s = sound(board.GP26)
print("Sound value=",l.readPin())

del s

# try moisture sensor
m = moisture(board.GP26)
print("Moist value=",l.readPin())

# try humidity sensor
h = humidity(board.GP4)
print("Humidity value=",l.getHumidity())
print("Temperature value=",l.getTemp())

#try MPU
g = MPU(board.GP6,board.GP7)
print("Acc:",g.getAcc())
print("Gyro:",g.getGyro())
print("Temperature:",g.getTemp())


