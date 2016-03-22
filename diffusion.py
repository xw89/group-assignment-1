# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 15:59:36 2016

"""

from pylab import*
from scipy.optimize import curve_fit
# initialize
dx = 0.1
dt = 0.002
D = 2
L = 100
T = 150
N = int(L/dx)
step = int(T/dt)
x = linspace(-L,L,2*N+1)
density = np.zeros([step+1, 2*N+1])
# box profile for the 11 points nearest to the origin at t=0
for i in range(N-5,N+5):
    density[0][i] = 1
# diffusion time revolution equation 
for k in range(step):
    for i in range(1,2*N):
        density[k+1][i] = density[k][i] + (density[k][i-1]+density[k][i+1]-2*density[k][i])*D*dt/dx**2

# use curve_fit to fit data to gaussian
# first define gaussian distribution
def gauss(x,*p):
    A,mu,sigma = p
    return A*np.exp(-(x-mu)**2/(2.0*sigma**2))
pini = [0.05,0,10] # initial guess for parameters
para = np.zeros([5,3])
for i in range(5):
    para[i],meiyong = curve_fit(gauss,x,density[int(30*(i+1)/dt)],p0=pini)
# get the optmized gaussian distribution with the parameter we justed fitted
density_opt = np.zeros([5,int(200/dx+1)])
for i in range(5):
    density_opt[i] = gauss(x,*para[i])

# plot 5 snap shot at 30s, 60s, 90s, 120s and 150s and optimized fitted gaussian
fig1 = plt.figure()
plot(x,density[int(30/dt)],'b',linewidth=3, label='30s')
plot(x,density[int(60/dt)],'r',linewidth=3, label='60s')
plot(x,density[int(90/dt)],'m',linewidth=3, label='90s')
plot(x,density[int(120/dt)],'g',linewidth=3, label='120s')
plot(x,density[int(150/dt)],'y',linewidth=3, label='150s')
legend()
for i in range(5):
    plot(x,density_opt[i],'k--')
xlabel('position')
ylabel('density')
fig1.savefig('diffusion.pdf')

# plot the function between sigma and sqrt(2Dt)
fig2 = plt.figure()
tsnap = np.arange(1,6,1)*30
sigma_th = sqrt(2*D*tsnap)
sigma_exp = para[:,2]
plot(sigma_th,sigma_exp,'ro')
plot([0.8*min(sigma_th),1.1*max(sigma_th)],[0.8*min(sigma_th),1.1*max(sigma_th)],'b--') # line of y=x (to compare sigma_th and sigma_exp)
xlabel('sqrt(2Dt)')
ylabel('sigma')
fig2.savefig('sigma.pdf')

show()
