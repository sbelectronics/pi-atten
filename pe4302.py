import RPi.GPIO as IO
import time

PE4302_LE = 2
PE4302_CLK = 3
PE4302_DATA = 4

class PE4302(object):
    def __init__(self, le=PE4302_LE, clk=PE4302_CLK, data=PE4302_DATA):
        self.le = le
        self.clk = clk
        self.data = data

        IO.setmode(IO.BCM)
        IO.setup(self.le, IO.OUT)
        IO.setup(self.clk, IO.OUT)
        IO.setup(self.data, IO.OUT)

        IO.output(self.clk, 0)
        IO.output(self.le, 0)

    def set_value(self, value):
        mask = 32
        for i in range(0,6):
            if (value & mask):
                IO.output(self.data, 1)
            else:
                IO.output(self.data, 0)

            # tick the clock
            IO.output(self.clk,1)
            time.sleep(0.01)
            IO.output(self.clk,0)
            time.sleep(0.01)

            mask = mask >> 1

        # load the latch
        IO.output(self.le, 1)
        time.sleep(0.01)
        IO.output(self.le, 0)






