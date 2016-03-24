from numpy import *
from pylab import *
from math import *
from random import *

n = 20            # number of radius values
#R = linspace(50, 300, n)  # radius
R =100


################################################################################
# function t calculate mass of cluster for given R values
def mass(r):

    mass = -1
    for i in range(2*R):
	    for j in range(2*R):
		    if (i-R)**2+(j-R)**2 < r**2 and P[i,j]==1 :
			    mass += 1
    #print "mass = " + str(mass)
    # extract fractal dimension df
    #df = log(mass)/log(R)

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
    max_distance = 0.0 # distance of farthest point in cluster from origin
    while max_distance < R:
    	theta = 2*pi*random()
    	xt = int(R + R*cos(theta))
    	yt = int(R + R*sin(theta))
    	flag = 1
    	while flag == 1:
    		p = random()			#2D random walk
    		if p < 0.25:
    			right = 1
    			xt = xt + 1

    		elif p < 0.5:
    			left = 1
    			xt = xt - 1

    		elif p < 0.75:
    			up = 1
    			yt = yt + 1

    		else :
    			down = 1
    			yt = yt - 1

    		# give up if further than 1.5R away from origin
    		dist_sq = (xt-R)**2+(yt-R)**2
    		if dist_sq > (1.5*R)**2:
    			break

    		###################################
    		### Attach the particle ar [xt,yt]#

    		# first make sure particle is inside circle to avoid index errors
    		if xt < 2*R and xt >= 0 and yt < 2*R and yt >= 0:

    			if P[xt+1, yt] == 1:
    				P[xt, yt] = 1
    				flag = 0
    			if P[xt-1, yt] == 1:
    				P[xt, yt] = 1
    				flag = 0
    			if P[xt, yt+1] == 1:
    				P[xt, yt] = 1
    				flag = 0
    			if P[xt, yt-1] == 1:
    				P[xt, yt] = 1
    				flag = 0

    			# check the size of the cluster
    			if flag == 0:
    				if dist_sq > max_distance**2:
    					max_distance = sqrt(dist_sq)
    					print 'Cluster size: ' + str(max_distance)

    	k += 1


    Mass = zeros(n) # initialize mass and fractional vectors
    rr = linspace(10,R,num=n)

    for i in range(n):
        Mass[i] = mass(int(rr[i]))

    # fit the curve on a log log scale to calculate fractional dimension
    # mass dependence on r can only be calculated for r <= Rmax/2
    logR = [log(x) for x in rr[0:int(n/2)]]
    logM = [log(x) for x in Mass[0:int(n/2)]]
    c = polyfit(logR,logM,deg=1) # coefficients of linear fit on log log scale
    slope = c[0] # slope of the fit
    polynomial = poly1d(c)
    fit = [exp(x) for x in polynomial(logR)]

    # save the slope
    Df_vals[j] = slope

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
