#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 13:06:13 2018

@author: vmatusic
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile
from scipy.stats import signaltonoise

from scipy.signal import argrelextrema
from pylab import *
import operator


fs=44100

rate, Tx1 = scipy.io.wavfile.read('sent_CSNDSP.wav')
norm_factor=max(Tx1)
Tx1=Tx1/norm_factor


#https://audio.online-convert.com/convert-to-wav

rate, Rx1 = scipy.io.wavfile.read('received_50cm.wav')
rate, Rx2 = scipy.io.wavfile.read('received_100cm.wav')
rate, Rx3 = scipy.io.wavfile.read('received_150cm.wav')
#rate, Rx4 = scipy.io.wavfile.read('received_cm.wav')
#rate, Rx5 = scipy.io.wavfile.read('received_125cm.wav')

WL = 441  #window length

window_time = np.linspace(0,WL/rate,num=WL)
window_time = window_time*1000
#window_time = window_time/44100

d1 = 0       #displacement
d2 = 6
d3 = 46

norm_factor=max(Rx1)
print(norm_factor)
Rx1=Rx1[d1:d1+WL]/norm_factor
norm_factor=max(Rx2)
print(norm_factor)
Rx2=Rx2[d2:d2+WL]/norm_factor
norm_factor=max(abs(Rx3))
print(norm_factor)
Rx3=Rx3[d3:d3+WL]/norm_factor



def SNR(signal):
    max_index, max_value = max(enumerate(signal), key=operator.itemgetter(1))
    leftsignal = signal[0:max_index];
    rightsignal = signal[max_index:];

    leftMin = array(leftsignal);
    rightMin = array(rightsignal);

    findLMin = argrelextrema(leftMin, np.less)[0][-1];
    findRMin = argrelextrema(rightMin, np.less)[0][0]+len(leftsignal);

    x = np.linspace(0, 100,len(signal));



    Anoise = np.mean(list(signal[0:findLMin])+list(signal[findRMin:]))
    #Asignal = 1-(signal[findLMin]+signal[findRMin])/2
    Asignal = 1-Anoise;

    snr_value = 20*np.log10(Asignal/Anoise);

    plot(x[0:findLMin], signal[0:findLMin],'b')
    plot(x[findLMin:findRMin],signal[findLMin:findRMin],'r')
    plot(x[findRMin:],signal[findRMin:],'b');
    plot([x[max_index], x[max_index]],[1, 1- Asignal],'r--');
    plot(x, x*0+Anoise,'b--');
    show();

    print(snr_value)
    return snr_value;

print(SNR(Rx1))
print(SNR(Rx2))
print(SNR(Rx3))




plt.subplot(4,1,1)
pltx1, = plt.plot(window_time, Tx1[:WL], 'blue', linewidth=1.0, label='True')
#plt.grid(True)
plt.xticks([])
#pltx2, = plt.plot(window_time, Rx1[d:d+WL], 'red', linewidth=2.0, label='True')
#plt.title('Comparision of 1kHz sine communicated through\n the VLC module varying Tx-Rx distance $d$.')
#plt.xlabel('t$[ms]$')
#plt.ylabel('Sent (1kHz)', fontsize = 8)

plt.subplot(4,1,2)
#pltx1, = plt.plot(window_time, Tx1[:WL], 'blue', linewidth=2.0, label='True')
pltx2, = plt.plot(window_time, Rx1, 'red', linewidth=1.0, label='True')
#plt.grid(True)
plt.xticks([])
#plt.xlabel('t')
#plt.ylabel('$d=.5m$', fontsize = 8)

#plt.legend([pltx1, pltx2], ['$original$ $message$', '$received$ $message$'])
plt.subplot(4, 1, 3)
#pltx1, = plt.plot(window_time, Tx1[:WL], 'blue', linewidth=2.0, label='True')
pltx3, = plt.plot(window_time, Rx2, 'green', linewidth=1.0, label='True')
#plt.grid(True)
plt.xticks([])
#plt.xlabel('t')
plt.ylabel('Normalized Amplitude')
#plt.ylabel('$d=1m$', fontsize = 8)

#plt.legend([pltx1, pltx2], ['$original$ $message$', '$received$ $message$'])
plt.subplot(4, 1, 4)
#pltx1, = plt.plot(window_time, Tx1[:WL], 'blue', linewidth=2.0, label='True')
pltx4, = plt.plot(window_time, Rx3, 'brown', linewidth=1.0, label='True')
#plt.grid(True)

plt.xlabel('time $[ms]$')
#plt.ylabel('$d=1.5m$', fontsize = 8)
x1,x2,y1,y2 = plt.axis()
plt.axis((x1,x2,-1,1))


plt.legend([pltx1, pltx2, pltx3, pltx4], ['Sent ($1kHz$ sine)', 'Received at $d=.5m$', 'Received at $d=1m$', 'Received at $d=1.5m$'])

#plt.grid(True)
plt.savefig('signal_against_distance.pdf')
#pdf.close()









