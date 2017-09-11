import pylab
import pywt

'''
Daubechies (db)
Symlets (sym)
Coiflets (coif)
Reverse biorthogonal (rbio)
'''

[psi, x] = pywt.ContinuousWavelet('morl').wavefun(level=6)

pylab.plot(x, psi)
pylab.show()
