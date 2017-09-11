from wavelets import wavelets
import matplotlib.pyplot as plt
import numpy as np



class MyCustomWavelet(object):
    def __init__(self, w0=6):
        self.w0 = w0
        if w0 == 6:
            # value of C_d from TC98
            self.C_d = 0.776

    def __call__(self, *args, **kwargs):
        return self.time(*args, **kwargs)

    def time(self, t, s=1.0, complete=True):

        w = self.w0

        x = t / s

        output = np.exp(1j * w * x)

        output *= np.exp(-2 * (x ** 2)) * np.pi ** (-0.5)

        return output

    # Fourier wavelengths
    def fourier_period(self, s):
        return 4 * np.pi * s / (self.w0 + (2 + self.w0 ** 2) ** .5)

    def scale_from_period(self, period):
        # Solve 4 * np.pi * scale / (w0 + (2 + w0 ** 2) ** .5)
        #  for s to obtain this formula
        coeff = np.sqrt(self.w0 * self.w0 + 2)
        return (period * (coeff + self.w0)) / (4. * np.pi)

    # Frequency representation
    def frequency(self, w, s=1.0):

        x = w * s
        # Heaviside mock
        Hw = np.array(w)
        Hw[w <= 0] = 0
        Hw[w > 0] = 1
        return np.pi ** -.25 * Hw * np.exp((-(x - self.w0) ** 2) / 2)

    def coi(self, s):
        return 2 ** .5 * s

a = MyCustomWavelet()
c = np.arange(-5.0, 5.0, 0.5)
d = []
for f in c:
    d.append(a.time(f))
plt.plot(c, d)
plt.show()
