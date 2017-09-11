import matplotlib.pyplot as plt
import numpy as np

with open('signal.dtu', 'r') as text_file:
    signal, time = [], []
    for line in text_file:
        arr = []
        for value in line.strip().split('\t'):
            try:
                value = float(value.strip('﻿'))
                arr.append(value)
            except ValueError:
                break
        if not len(arr) == 0:
            time.append(arr[0])
            signal.append(arr[6])
# given a signal x(t)
# x = np.random.randn(1000)

y = time
x = signal
plt.plot(y, x)
plt.xlabel('Seconds')
plt.ylabel('mV')
plt.show()
