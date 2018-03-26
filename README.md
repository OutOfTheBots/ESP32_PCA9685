# ESP32_PCA9685

This is a light weight servo driver for Micro-Python running Laboris port on a ESP32.
All servo positons are in radians to make for light transacion with python trigonometry fucitons
Signal freq is set at 50Hz as is ideal for most common hobby seros.
Default salve address is )x40 but can be set duing initialization 
Default I2C bus speed is 1Mhz but can also be set during initialization.
The driver is designed as super light weight fast lower level driver without error checking.
All eeror checking will need to be done at a higher level by user program.
