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
turtle.color("blue")
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
		###################################
		### Attach the particle ar [xt,yt]# 
		if xt+1 <= 2*R and P[xt+1, yt] == 1:
			P[xt, yt] = 1
			turtle.goto((xt-R)*10,(yt-R)*10)
			turtle.stamp()	
			flag = 0
		if xt-1 >= 0 and P[xt-1, yt] == 1:
			P[xt, yt] = 1
			turtle.goto((xt-R)*10,(yt-R)*10)
			turtle.stamp()	
			flag = 0
		if yt+1 <= 2*R and P[xt, yt+1] == 1:
			P[xt, yt] = 1
			turtle.goto((xt-R)*10,(yt-R)*10)	
			turtle.stamp()		
			flag = 0
		if yt-1 <= 2*R and P[xt, yt-1] == 1:
			P[xt, yt] = 1
			turtle.goto((xt-R)*10,(yt-R)*10)
			turtle.stamp()			
			flag = 0
	k += 1	
	print str((k*100.0/Nmax))+"% completed"

turtle.exitonclick()
