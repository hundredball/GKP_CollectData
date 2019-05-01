#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 12:54:24 2018

@author: hundredball
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

def butter_highpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='high', analog=False)
    return b, a

def butter_highpass_filter(data, cutoff, fs, order=5):
    b, a = butter_highpass(cutoff, fs, order=order)
    y = filtfilt(b, a, data)
    return y

plt.figure(0)
for i in range(0,16):
    plt.plot(data[i])

fs = 125.0
cutoff = .5
order = 6
plt.figure(1)
for i in range(0,16):  
    signal = data[i]
    conditioned_signal = butter_highpass_filter(signal, cutoff, fs, order)
    plt.plot(conditioned_signal)
    plt.hold(True)