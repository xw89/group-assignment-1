# -*- coding: utf-8 -*-
"""
Created on Thur Mar 17 2016

"""


import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

global dx, D, L, N, x, density0, density,dt,t,T
dx = 0.1
D = 2.0			#Diffusion constant
L = 10.0		#half length 
N = int(L/dx)
x = np.linspace(-L, L, 2*N+1)
density0 = np.zeros(2*N+1)	#rho_0
density = np.zeros(2*N+1)	#new rho
dt = 5e-4
t = 0.0				#initial t
T = 1.0				#total t

fig = plt.figure()
ax = plt.axes(xlim=(-L, L), ylim=(0, 1.05))
line, = ax.plot([], [], lw=2)
time_text = ax.text(0.02, 0.96, '', transform=ax.transAxes)		#show time
plt.xlabel('x (m)')
plt.ylabel('density($\\rho$)')
plt.title("Solution of diffusion equation") 

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text

# animation function.  This is called sequentially
def animate(k):
    global density,t,density0
    t += dt
    if t<=T:  				#stop when t>T(in display)
        line.set_data(x, density0)
        time_text.set_text('time = %.3f' % t+'s')
        for i in range(1,2*N):
            density[i] = density0[i] + (density0[i-1]+density0[i+1]-2.0*density0[i])*D*dt/dx**2
        (density0, density) = (density, density0)
    return line, time_text

# box profile for the 11 points nearest to the origin at t=0
for i in range(N-5, N+5):
    density0[i] = 1

# call the animator.  blit=True means only re-draw the parts that have changed.
ani = animation.FuncAnimation(fig, animate, frames=800,
                              interval=1, blit=True, init_func=init)
ani.save('diffusion.mp4', writer='ffmpeg', fps=30, dpi=120) #save the animation

