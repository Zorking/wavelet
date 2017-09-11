import numpy as np
import matplotlib.pyplot as plt

from wavelets import WaveletAnalysis

with open('signal.dtu', 'r') as text_file:
    signal = []
    for line in text_file:
        arr = []
        for value in line.strip().split('\t'):
            try:
                value = float(value.strip('﻿'))
                arr.append(value)
            except ValueError:
                break
        if not len(arr) == 0:
            signal.append(arr[6])
# given a signal x(t)
# x = np.random.randn(1000)
x = np.array(signal)
# and a sample spacing
dt = 0.00025

wa = WaveletAnalysis(x, dt=dt)

# wavelet power spectrum
power = wa.wavelet_power

# scales
scales = wa.scales

# associated time vector
t = wa.time

# reconstruction of the original data
rx = wa.reconstruction()

fig, ax = plt.subplots()
T, S = np.meshgrid(t, scales)
ax.contourf(T, S, power, 100)
ax.set_yscale('log')
fig.savefig('test_wavelet_power_spectrum.png')
