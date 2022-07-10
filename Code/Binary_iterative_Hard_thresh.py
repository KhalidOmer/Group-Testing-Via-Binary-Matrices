# importing the required library 
import matplotlib.pyplot as plt
import numpy as np

####################################
"""the function simulate randomy generates
 the design matrix A, vector x, and binarized vector of their product y"""

def simulate_input(m,n,d):
    x = np.zeros(n) #Here we generate zeros
    x[:d] = 1 #turn some of zeros into ones, the portion is specified by d  
    np.random.shuffle(x) # the shuffle function places these one randomly
    #x = np.array(a, dtype = bool) you do not need this
    A = np.mod(np.random.permutation(m*n).reshape(m,n),2) # random bianry matrix  
    u = np.dot(A,x)# the product of A and x
    y = np.sign(u)  # binary of the product
    return A, x, y

 ####################################
"""The function prunc takes a vector x and returns 
   a vector xk with the k largest
   in magnitude entries of x not set to zero"""

 def prunc(x, k):
    indices = np.argsort(np.abs(x))[::-1]
    largest = indices[0:k]
    xk = np.zeros(len(x))
    for kl in largest:
        xk[kl] = x[kl]
    return xk

###############################################
"""The biht function performs one-bit compressive sensing 
    via the Binary Iterative Hard Thresholding algorithm
     and returns the recoverd vector x_bar"""

def biht(A, y, d):
    m, n = A.shape
    x_bar = np.zeros(n)
    tau = 0.001 # step size for gradient update
    tol = 10E-16 # stoping criteria 
    i = 0 
    while i < 1000:
        i = i+1
        dif = y - np.sign(np.dot(A, x_bar))
        temp = x_bar + (tau/2)*np.dot(np.transpose(A), dif)
        x1 = prunc(temp, d)
        err = np.subtract(x1, x_bar)
        assert(x1.shape == x_bar.shape)
        if np.linalg.norm(np.abs(err)) < tol:
            break
        x_bar = x1

    x_bar = [1.0 if x_bar[i] > 0 else 0.0 for i in range(len(x_bar))]
    return np.array(x_bar)

#####################################################################

"""The following are three performance tests"""

#The sigma test 

#Here we check sigma vs m
n  = 100
d = 2
co = []
for m in np.arange(10,n,5):
    for i in range(10): 
        A, x, y = simulate_input(m, n ,d)
        xbar = biht(A, y, d)
        #print(x)
        #print(xbar)
        count = 0
        for j in range(len(xbar)):
            if xbar[j] != x[j]: 
                count = count+1
    co.append(count)


#The exact recovery test, the false positive and the false negative test

exa =[]
faln = []
falp = []
d = 4 # assume there are only d defectives
n = 512 # the total number of individuals being tested
#m = number of tests

for m in np.arange(10,n,5):
  count = 0
  neg = 0 
  pos = 0 
  for k in np.arange(100):
        A, x, y = simulate_input(m, n, d)
        xbar = biht(A,y,d)
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

#########################################################

"""The graphs from the tests"""
#The sigma vs m test 
x = np.arange(10,n,5)
#  separate plot for the error sigma  
plt.plot(x,co, 'b', label = "$\sigma$")
plt.xlabel('Number of tests (m)')
plt.ylabel('$\sigma$')
plt.legend()
plt.show()

########
#the exact recovery and the false positives and negaives vs m

x = np.arange(10,n,5)
# plot of false positive and false negatives 
plt.plot(x,faln,'r', label = 'False negatives')
plt.plot(x,falp, 'b', label = 'False positives')
plt.xlabel('Number of tests')
plt.ylabel('Average number')
#plt.title("The number of exactly recovered vectors vs different values of m")
plt.legend()
plt.show()
##########
#  separate plot for the exact recovery 
plt.plot(x,exa, 'g', label = "Exact recovery")
plt.xlabel('Number of tests')
plt.ylabel('Probability of perfect recovery')
plt.legend()
plt.show()

