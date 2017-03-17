import pywt

cA, cD = pywt.dwt([2000, 2400, 1800, 2399], 'db1')
print cA
print cD
