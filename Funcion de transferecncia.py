from matplotlib import pyplot as plt
import numpy as np
wc=2
init=0.1
ending=100
Npasos=int(input("Ingrese pasos"))
w=np.linspace(init,ending,Npasos)
magH=20*np.log10((w/wc)/((w/wc)**2+1)**(1/2))
plt.plot(w,magH)
plt.scatter([wc],[-3.01])
plt.show()
