import pylab
import pywt

'''
Daubechies (db)
Symlets (sym)
Coiflets (coif)
Reverse biorthogonal (rbio)
'''

[phi, psi, x] = pywt.Wavelet('db1').wavefun(level=4)

pylab.plot(x, psi)
pylab.show()
