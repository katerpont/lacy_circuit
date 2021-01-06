import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import math

#initial
v0 =1.5
f =9200
Y_in = [0.5, 0.1]
C = 62.9 * (10 ** -9)
L = 32.9 * (10 ** -3)
R = 700
Ga = -0.00135
Gb = 0.005
Bp = 1.82
a = R*Ga
bl = R*Gb
bg = (C*(R**2))/L
B = v0*bg/Bp
w = 2*np.pi*f*R*C
NN = 2
tp = 1/(f*R*C)
NIT = 1000
NTR = 10000
tstep = tp/NIT
xmax = 3
xmin = -3
ymax = 3
ymin = -3
xstep = (xmax-xmin)/10
ystep = (ymax-ymin)/10
t = 0

def yprim(Y, yprim_k_helper):
    if Y[0] >= 1:
        gx = bl*Y[0]+a-bl

    if Y[0] <= -1:
        gx = bl*Y[0]-a+bl

    if Y[0] > -1 and Y[0] < 1:
        gx = a*Y[0]

    if yprim_k_helper == 0:
        YPRIM = Y[1]-gx

    if yprim_k_helper == 1:
        YPRIM = -bg*Y[1]-bg*Y[0]+B*math.cos(w*t)

    return YPRIM

def RKK4():
    y1list = []
    YY1list = []
    y2list = []
    YY2list = []
    y3list = []
    YY3list=[]
    y4list = []
    YNEWlist = []
    for k in range(0, 2):
        y1 = tstep*yprim(Y_in, k)
        y1list.append(y1)
    for k in range(0, 2):
        YY1 = Y_in[k] + y1list[k]/2
        YY1list.append(YY1)
    for k in range(0, 2):
        y2 = tstep*yprim(YY1list, k)
        y2list.append(y2)
    for k in range(0, 2):
        YY2 = Y_in[k]+y2list[k]/2
        YY2list.append(YY2)
    for k in range(0, 2):
        y3 = tstep*yprim(YY2list, k)
        y3list.append(y3)
    for k in range(0, 2):
        YY3 = Y_in[k]+y3list[k]
        YY3list.append(YY3)
    for k in range(0, 2):
        y4 = tstep*yprim(YY3list, k)
        y4list.append(y4)
    for k in range(0, 2):
        YNEW = Y_in[k] + (y1list[k] + 2*y2list[k] + 2*y3list[k] + y4list[k])/6
        YNEWlist.append(YNEW)
    return YNEWlist

YNEW1 = []
YNEW2 = []
rkk4list = []

for i in range(100000):
    rkk4list = RKK4()
    t = t + tstep
    Y_in = rkk4list
    if i> NTR:
        YNEW1.append(rkk4list[0])
        YNEW2.append(rkk4list[1])

final = [YNEW1, YNEW2]
axis = [xmin, xmax, ymin, ymax]

plt.plot(final[0], final[1], color='black', marker=',', linewidth='0.1',markersize='1')
plt.axis(axis)
plt.show()


