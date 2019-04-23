

"""
more physics with python
numpy for the maths stuff - sine,cosine,pi
linspace - makes an array, range and then the numbers inside them
like 10000 numbers between 0,50
odeint is for first order diff eqs, integrates it wrt 't'
lorenz1[:,0], colon says all rows and 0,1,2 tells the column
"""
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


s=10
r=28
b=8/3
vec1=(0,1,0)
t=np.linspace(0,50,10000)

def fd(x):
    print(x)
    

fd(4)

def fg(vec,t):
    x,y,z = vec
    
    dxdt = s*(y-x)
    dydt = r*x-y-x*z
    dzdt = x*y-b*z
    
    return dxdt,dydt,dzdt

lorenz1 = odeint(fg,vec1,t)

x1 = lorenz1[:,0]
y1 = lorenz1[:,1]
z1 = lorenz1[:,2]

plt.plot(x1,y1)
plt.show()