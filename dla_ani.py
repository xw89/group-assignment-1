import turtle
from numpy import *
from math import *
from random import *

R = 100			#radius
P = zeros([2*R+1, 2*R+1])	#2D array to plot
Nmax = 1000			#max steps
k = 0
P[R,R] = 1			#origin is one
turtle.penup()
turtle.shape("circle")
turtle.shapesize(0.2,0.2)
turtle.color("red")
turtle.goto(0,0)
turtle.stamp()
turtle.color("blue")
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
		if dist_sq > (1.1*R)**2:
			break

		###################################
		### Attach the particle ar [xt,yt]#

		# first make sure particle is inside circle to avoid index errors
		if xt < 2*R and xt >= 0 and yt < 2*R and yt >= 0:
			if P[xt+1, yt] == 1:
				P[xt, yt] = 1
				flag = 0
				turtle.goto((xt-R)*4,(yt-R)*4)
				turtle.stamp()	
			if P[xt-1, yt] == 1:
				P[xt, yt] = 1
				flag = 0
				turtle.goto((xt-R)*4,(yt-R)*4)
				turtle.stamp()	
			if P[xt, yt+1] == 1:
				P[xt, yt] = 1
				flag = 0
				turtle.goto((xt-R)*4,(yt-R)*4)
				turtle.stamp()	
			if P[xt, yt-1] == 1:
				P[xt, yt] = 1
				flag = 0
				turtle.goto((xt-R)*4,(yt-R)*4)
				turtle.stamp()	
			# check the size of the cluster
			if flag == 0:
				if dist_sq > max_distance**2:
					max_distance = sqrt(dist_sq)
					print 'Cluster size: ' + str(max_distance)
	k += 1	

print "Done!"
turtle.exitonclick()
