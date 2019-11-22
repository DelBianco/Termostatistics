import numpy as np
from walker import Walker
import matplotlib.pyplot as plt

N = int(10E5)
w = Walker(0)

datFile = file('out.dat','w')
histFile = file('histogram.dat','w')

hist = []

for i in range(0,N):
    w.walk()
    hist.append(w.getX())
    datFile.write(str(i) +'\t'+ str(w) + '\n')

hist.sort()
h = []
change = 0
counter = 0
for i in hist:
    if(counter == 0 or change != i):
        change = i
        h.append({'key': i, 'value': counter})
        counter = 0
    counter += 1

for pos in h:
    histFile.write(str(pos['key']) +'\t'+ str(pos['value']) + '\n')