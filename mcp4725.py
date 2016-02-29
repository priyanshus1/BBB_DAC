from Adafruit_I2C import Adafruit_I2C
import numpy as np
import time


class DAC:
    
    RESOLUTION = 2**12 - 1
    WRITE_REGISTER = 0x40

    # Set the address to the default
    def __init__(self, address=0x60):
        self.i2c = Adafruit_I2C(address)
        
    # Send the voltage in two bytes
    def send_voltage(self, bits):
        bytes = [(bits >> 4) & 0xFF, (bits << 4) & 0xFF]
        self.i2c.writeList(self.WRITE_REGISTER, bytes)

    # Limit the max and min voltage that can be set
    # and convert to the resolution of the dac
    def set_voltage(self, voltage):
        if voltage > 100:
            voltage = 100
        elif voltage < 0:
            voltage = 0

        bits = int(voltage/100. * self.RESOLUTION)
        self.send_voltage(bits)


def test_run():
    dac = DAC()
    # sin(t*f*2*pi) w\ f = frequency
    sig = lambda t: 50*np.sin(t*5*2*np.pi) + 50
    start_time = time.time()

    while True:
        dac.set_voltage(sig(time.time()-start_time))
test_run()
