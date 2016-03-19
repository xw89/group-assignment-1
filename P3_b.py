from numpy import *
from pylab import *
from math import *
from random import *

Nmax = 5000	     # max steps    
n = 5            # number of radius values
R = linspace(50, 300, n)  # radius
####################################################################################
# function t calculate mass of cluster for given R and Nmax values
def mass(R,Nmax):
    P = zeros([2*R+1, 2*R+1])	#2D array to plot
    k = 0
    P[R,R] = 1			#origin is one
    while k < Nmax:
	    r = R*random()
	    theta = 2*pi*random()
	    xt = int(R + R*cos(theta))
	    yt = int(R + R*sin(theta))
	    flag = 1
	    while flag == 1:
		    p = random()			#2D random walk
		    if p < 0.25:
			    right = 1
			    xt = xt + 1
			    if xt > 2*R :
				    xt = xt - R
		    elif p < 0.5:
			    left = 1
			    xt = xt - 1
			    if xt < 0 :
				    xt = xt + R
		    elif p < 0.75:
			    up = 1
			    yt = yt + 1
			    if yt > 2*R :
				    yt = yt - R
		    else :
			    down = 1
			    yt = yt - 1
			    if yt < 0 :
				    yt = yt + R	
		    if (xt-R)**2+(yt-R)**2>R**2:		#out of the circle
			    continue
		### Attach the particle to [xt,yt]# 
		    if xt+1 <= 2*R and P[xt+1, yt] == 1:
			    P[xt, yt] = 1		
			    flag = 0
		    if xt-1 >= 0 and P[xt-1, yt] == 1:
			    P[xt, yt] = 1		
			    flag = 0
		    if yt+1 <= 2*R and P[xt, yt+1] == 1:
			    P[xt, yt] = 1		
			    flag = 0
		    if yt-1 <= 2*R and P[xt, yt-1] == 1:
			    P[xt, yt] = 1		
			    flag = 0
	    k += 1	
	    print str((k*100.0/Nmax))+"% completed"

    ################
    # count mass

    mass = -1
    for i in range(2*R):
	    for j in range(2*R):
		    if (i-R)**2+(j-R)**2 < R**2 and P[i,j]==1 :
			    mass += 1          
    print "mass = " + str(mass)
    # extract fractal dimension df
    #df = log(mass)/log(R)
    
    return mass
####################################################################################################################



Mass = zeros(n) # initialize mass and fractional vectors
Df = zeros(n)

for i in range(n):
    Mass[i] = mass(int(R[i]), Nmax)
    Df[i] = log(Mass[i])/log(R[i])
     
print array(Mass)
print array(Df)
# plot fractional dimention
figure(1)
plot(R, Mass, 'm-')
plt.xlabel('R')
plt.ylabel('mass')
plt.title("mass vs. R")
plt.show()
savefig('mass_vs_R.pdf')
savefig('mass_vs_R.eps')

figure(2)
plot(R, Df, 'g-')
plt.xlabel('R')
plt.ylabel('Df')
plt.title("fractional dimention")
plt.show()
savefig('fractional_dimension.pdf')
savefig('fractional_dimension.eps')