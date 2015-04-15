#!/usr/bin/env python

__author__ = 'infused'

import sys
from time import sleep
from redpitaya_scpi import scpi

rp_s = scpi (sys.argv[1])

#Generate signal
rp_s.gen (src=1, waveform='sine', freq=50000, ampl=1)

rp_s.send_txt('ACQ:SOUR1:GAIN LV')
rp_s.send_txt('ACQ:DEC 1'       )
rp_s.send_txt('ACQ:TRIG:LEV 100')
rp_s.send_txt('ACQ:START'       )
rp_s.send_txt('ACQ:TRIG CH1_PE' )
while 1:
    rp_s.send_txt('ACQ:TRIG:STAT?')
    if rp_s.recv_txt(4) == 'TD':
        break
rp_s.send_txt('ACQ:SOUR1:DATA?')
buff_string = rp_s.recv_txt()
buff_string = buff_string.strip('{} ').split(',')
buff = map(float, buff_string)

# check trigger settings
rp_s.send_txt('ACQ:TRIG:DLY?')
print('ACQ:TRIG:DLY? = ' + rp_s.recv_txt())

rp_s.send_txt('ACQ:SOUR1:GAIN?')
print('ACQ:SOUR1:GAIN = ' + rp_s.recv_txt())

import matplotlib.pyplot as plt
plt.plot(buff)
plt.ylabel('Voltage')
plt.show()