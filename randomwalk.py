# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 15:35:28 2016


"""
from pylab import*
# an array for random numbers(10000*100)
random=np.random.rand(10000,100)
# initialize four array to record the x and y position and x^2, y^2 for the 10000 walkers
x=np.zeros([10000,101])
y=np.zeros([10000,101])
xsq=np.zeros([10000,101])
ysq=np.zeros([10000,101])
# four arrays for to record average among walkers of the 100 steps
xav=np.zeros(101)
yav=np.zeros(101)
xsqav=np.zeros(101)
ysqav=np.zeros(101)
rsqav=np.zeros(101)
# loop over 10000 walkers for 100 steps
for i in range(100): # if random [0,0.25),x+1; if  [0.25,0.5),x-1; if [0.5,0.75), y+1, if  [0.75,1],y-1     
    for k in range(10000):        
        if random[k][i]<0.25:
            x[k][i+1]=x[k][i]+1
            y[k][i+1]=y[k][i]
        elif random[k][i]<0.5:
            x[k][i+1]=x[k][i]-1
            y[k][i+1]=y[k][i]
        elif random[k][i]<0.75:
            x[k][i+1]=x[k][i]
            y[k][i+1]=y[k][i]+1
        else:
            x[k][i+1]=x[k][i]
            y[k][i+1]=y[k][i]-1
        xsq[k][i]=(x[k][i])**2
        ysq[k][i]=(y[k][i])**2
    xav[i]=sum(x[:,i])/10000
    yav[i]=sum(y[:,i])/10000
    xsqav[i]=sum(xsq[:,i])/10000
    ysqav[i]=sum(ysq[:,i])/10000
    rsqav[i]=xsqav[i]+ysqav[i]
"""
part a, figure for x_n and x_n^2
"""
t=range(101)
fig1=plt.figure()
plot(t,xav,'ro')
plot(t,xsqav,'gx')
xlabel('Steps')
ylabel('x and x^2')
legend(['x_n average','x^2_n average'])
fig1.savefig('C:\\Users\\Xinyu Wu\\Desktop\\566\\my work\\group_assignment_1\\rwxn.pdf') # the path in my computer

"""
part b, figure for rn^2 
"""
fig2=plt.figure()
plot(t,rsqav,'ro')
xlabel('Steps')
ylabel('Distance^2')
fig2.savefig('C:\\Users\\Xinyu Wu\\Desktop\\566\\my work\\group_assignment_1\\rwxn.pdf') # path in my computer

