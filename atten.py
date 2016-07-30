import spidev
import sys
import time

from vfd import *
from encoder import *
from pe4302 import *

def vfd_update(vfd, value):
            vfd.setPosition(0,0)
            vfd.writeStr("Attenuation")
            vfd.setPosition(8,1)
            vfd.writeStr("%0.1f " % (0.5 * value))

def main():
    vfd = VFD(0,0)
    vfd.cls()

    value = 0

    vfd_update(vfd, value)

    encoder = EncoderWorker(RGBEncoder(ENCODER_PIN_A,
                                       ENCODER_PIN_B,
                                       ENCODER_PIN_SW,
                                       ENCODER_PIN_R,
                                       ENCODER_PIN_G,
                                       ENCODER_PIN_BLU))
    encoder.start()

    attenuator = PE4302()

    while 1:
        delta = encoder.get_delta()
        if delta!=0:
            value = min(63, max(0, value + delta))

            vfd_update(vfd, value)
            attenuator.set_value(value)

if __name__ == "__main__":
    main()
