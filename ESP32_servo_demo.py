from ESP32_PCA9685 import Servo


try:
  robot=Servo(27,26) #PCA9585 is connected to pin 27,26
  #set fir 3 servos to psition -pi/2 (-90 degrees)
  robot.set_servo(-pi/2, 0)
  robot.set_servo(-pi/2, 1)
  robot.set_servo(-pi/2, 2)
  #set next 3 servos to -pi/4 (-45 degrees)
  robot.set_servo(-pi/4, 3)
  robot.set_servo(-pi/4, 4)
  robot.set_servo(-pi/4, 5)
  #set next 3 servos to pi/4 (45 degress)
  robot.set_servo(-pi/2, 6)
  robot.set_servo(-pi/2, 7)
  robot.set_servo(-pi/2, 8)
  #set next 3 servos to pi/2 (90 degress)
  robot.set_servo(-pi/2, 9)
  robot.set_servo(-pi/2, 10)
  robot.set_servo(-pi/2, 12    

finally: robot.deinit() #deinit the I2C bus