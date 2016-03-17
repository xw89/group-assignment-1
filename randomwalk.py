# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 15:35:28 2016


"""
from pylab import*
import turtle

n = 105			#n steps
n_walk = 10000		#number of walkers

# initialize four array to record the x and y position and x^2, y^2 for the n_walk walkers
x = np.zeros([n_walk,n])
y = np.zeros([n_walk,n])
xsq = np.zeros([n_walk,n])
ysq = np.zeros([n_walk,n])
# four arrays for to record average among walkers of the n steps
xav = np.zeros(n-1)		#x average
yav = np.zeros(n-1)		#y average
xsqav = np.zeros(n-1)		#x^2 average
ysqav = np.zeros(n-1)		#y^2 average
rsqav = np.zeros(n-1)		#r^2 average

# loop over n_walk walkers for n steps
for i in range(n-1): # if random [0,0.25),x+1; if  [0.25,0.5),x-1; if [0.5,0.75), y+1, if  [0.75,1],y-1     
    for k in range(n_walk): 
	rd = np.random.rand()       
        if rd < 0.25:
            x[k][i+1] = x[k][i]+1	#right motion
            y[k][i+1] = y[k][i]
        elif rd < 0.5:
            x[k][i+1] = x[k][i]-1	#left motion
            y[k][i+1] = y[k][i]
        elif rd < 0.75:
            x[k][i+1] = x[k][i]		#up motion
            y[k][i+1] = y[k][i]+1
        else:
            x[k][i+1] = x[k][i]		#down motion
            y[k][i+1] = y[k][i]-1
        xsq[k][i] = (x[k][i])**2
        ysq[k][i] = (y[k][i])**2
    xav[i] = sum(x[:,i])/n_walk		
    yav[i] = sum(y[:,i])/n_walk		
    xsqav[i] = sum(xsq[:,i])/n_walk	
    ysqav[i] = sum(ysq[:,i])/n_walk	
    rsqav[i] = xsqav[i] + ysqav[i]	#r^2 = x^2 + y^2

#part a, figure for x_n and x_n^2
t = range(n-1)
fig1 = plt.figure()
plot(t,xav,'ro', label = '$<x_n>$ average')
plot(t,xsqav,'gx',label = '$<x^2_n>$ average')
grid()
xlabel('Steps(n)')
ylabel('$<x>$ and $<x^2>$')
legend(loc=2)
fig1.savefig('rwxn.pdf') 

#part b, figure for rn^2 
fig2 = plt.figure()
plot(t,rsqav,'.r', label = '$<r^2>$')
grid()
legend(loc=2)
xlabel('Steps(n)')
ylabel('$r^2$')
fig2.savefig('rwxn2.pdf') 

#Plot a 2D random walk figure 
fig3 = plt.figure()
plot(x[1,:],y[1,:])
title("2D Random Walk")
xlabel('x')
ylabel('y')
fig3.savefig('rwxn3.pdf') 
show()

#Animition in turtle
walk = [x[1,:],y[1,:]]
for x, y in zip(*walk):
    turtle.goto(x*30,y*30)		#x,y times 30 to make it clear to see each step

turtle.exitonclick()









