from matplotlib import pyplot
from math import log10

magH=[]
ws=[]
for i in range(1,101):
    ws.append(i*0.2)
print(list(ws))
for w in ws:
    wc=5
    magH.append(20*log10((w/wc)/((w/wc)**2+1)**(1/2)))


print(magH)

pyplot.plot(ws,magH)
pyplot.show()
