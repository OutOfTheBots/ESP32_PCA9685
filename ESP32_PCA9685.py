'''
Copyright (c) 2018 Out of the BOTS
MIT License (MIT) 
Author: Shane Gingell

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
ll copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

This file is is a light weight Micro-Python servo driver for the PCA9685 chipset
All servo updates are are staggered to lower current spikes
defaul slave address is 0x40 and default bus_speed is 1MHz, 
Servo position are in radians not degrees and servo signal freq is set at 50Hz.
'''


import machine, time
from ustruct import pack
from math import pi

class Servo:
  def __init__(self, sda, scl, slave=0x40, bus_speed=1000000):    
	self.slave = slave	
	self.i2c = machine.I2C(0, speed=bus_speed, sda=27, scl=26)    
	self.i2c.writeto_mem(slave, 0x00, b'\x10') #set mode1 to sleep    
	time.sleep_us(5)    
	prescale = int((25000000/ (4096*50))+0.5)    
	self.i2c.writeto_mem(slave, 0xfe, pack('B',prescale)) #setprescale    
	self.i2c.writeto_mem(slave, 0x00, b'\xa1') #set mode1 	
	time.sleep_us(5)    
	self.step = 200/(pi/2) #step size for radians	
	for servo in range(16):  #set all servos to popsition 0    
	  on_time = servo*220      
	  off_time = on_time + 340	  
	  self.i2c.writeto_mem(self.slave, 0x06 + (servo*4), pack('<HH', on_time, off_time))	

  def set_servo(self, pos, servo):
	off_time = (servo * 220) + 340 - (int(pos * self.step))     
	self.i2c.writeto_mem(self.slave, 0x08 + (servo*4), pack('<H',off_time))
	
  def deinit(self):
    self.i2c.deinit()


