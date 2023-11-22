from matplotlib import pyplot
import math


def Magnitud(w,wc):
    return 20*math.log10(1/(1+(w/wc)**2)**(1/2))


w=[i*0.01 for i in range(1,1001)]


H=[Magnitud(w_i,5) for w_i in w]

pyplot.plot(w,H)
pyplot.show()