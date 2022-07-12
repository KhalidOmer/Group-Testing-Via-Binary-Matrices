import numpy as np
import matplotlib.pyplot as plt

##############################################################
#Here is an example of the code, you can run it as a test
# examples 
# This is an example of no. of exactly recovered vs m
exa =[]
faln = []
falp = []
d = 2 # assume there are only d defectives
n = 100 # the total number of individuals being tested
#m = number of tests
k = 1000
for m in np.arange(10,n,5):
    count = 0
    neg = 0 
    pos = 0 
    for j in np.arange(100):
        A, x, y = outcome_vector(m,n,d)
        xbar = recovery(A,y,d,k)
        if (xbar==x).all() == True:
            count = count+1
        else: 
            for i in range(len(xbar)):
                if xbar[i] < x[i]:
                   neg = neg+1
                elif xbar[i] > x[i]: 
                    pos = pos+1
    exa.append(count/100)
    faln.append(neg/100)
    falp.append(pos/100)
###############################################################
"""Here are two graphs of the exactly recovered vs m abn false negative and false positive vs m"""

x = np.arange(10,n,5)
plot of false positive and false negatives 
plt.plot(x,faln,'r', label = 'False negatives')
plt.plot(x,falp, 'b', label = 'False positives')
plt.xlabel('Number of tests')
plt.ylabel('Average number')
plt.title("The number of exactly recovered vectors vs different values of m")
plt.legend()
plt.show()

#  separate plot for the exact recovery 
plt.plot(x,exa, 'g', label = "Exact recovery")plt.xlabel('Number of tests')
plt.ylabel('Probability of perfect recovery')
plt.legend()
plt.show()

##############################################################
