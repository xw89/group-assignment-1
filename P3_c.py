from numpy import *
from pylab import *
from math import *
from random import *

Nmax = 20000	     # max steps
n = 10            # number of radius values
#R = linspace(50, 300, n)  # radius
R =100


################################################################################
    # function t calculate mass of cluster P for given r and Nmax values

def mass(r,Nmax):

    # count mass
    mass = -1
    for i in range(2*R):
	    for j in range(2*R):
		    if (i-R)**2+(j-R)**2 < r**2 and P[i,j]==1 :
			    mass += 1

    return mass
################################################################################


################################################################################

# create 10 different clusters

Df_vals = zeros(10) # list to hold Df for each cluster

for j in range(10):

    print '\n \n iteration ' + str(j+1) + '\n \n'

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
        if (k % 1000) == 0:
            print str((k*100.0/Nmax))+"% completed"


    Mass = zeros(n) # initialize mass and fractional vectors
    Df = zeros(n)
    rr = linspace(10,R/2.0,num=n) # mass dependence on r can only be calculated for r <= Rmax/2

    for i in range(n):
        Mass[i] = mass(int(rr[i]), Nmax)
        Df[i] = log(Mass[i])/log(rr[i])

    # fit the curve on a log log scale to calculate fractional dimension
    logR = [log(x) for x in rr]
    logM = [log(x) for x in Mass]
    c = polyfit(logR,logM,deg=1) # coefficients of linear fit on log log scale
    slope = c[1] # slope of the fit
    polynomial = poly1d(c)
    fit = [exp(x) for x in polynomial(logR)]

    # save the slope
    Df_vals[j] = slope

    # plot mass dimension
    # figure(1)
    # loglog(rr, fit, 'r-',label=('Linear fit (slope = ' + '{0:.2f}'.format(slope) + ')'))
    # loglog(rr, Mass, 'ko',label='m(r) data')
    # plt.axis([10, 10**2, 10**2, 10**4])
    # plt.legend(loc='upper right')
    # plt.xlabel('r')
    # plt.ylabel('m(r)')
    # plt.title("Mass of a DLA cluster within a disk of radius r")
    # savefig('mass_vs_R_'+str(j+1)+'.pdf')
    # plt.clf()

    # plot clusters
    figure()
    print "Ploting..."
    for ii in range(2*R):
    	for jj in range(2*R):
    		if P[ii,jj]==1 :
    			plot(ii, jj, '.b')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('DLA cluster ' + str(j+1) )
    plt.savefig('dla_' +str(j)+'.pdf')
    print 'Saved ' + 'dla_' +str(j)+'.pdf'
    plt.clf()

# end loop

################################################################################

print Df_vals # print out the values for Df
print 'Avg Df: '+ str(sum(Df_vals) / float(len(Df_vals))) # print mean value
print 'standard deviation: '+str(std(asarray(Df_vals))) # print standard deviation