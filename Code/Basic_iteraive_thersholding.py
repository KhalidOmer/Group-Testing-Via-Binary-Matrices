import matplotlib.pyplot as plt
import numpy as np
"""There are three chunks of code here, the first generates the out come vector, the second works as a sorting tool, and the last is the recovery function"""
def outcome_vector(m,n,d):
    x = np.zeros(n)#Here we generate zeros
    x[:d] = 1 #turn some of zeros into ones, the portion is specified by d  
    np.random.shuffle(x) # the shuffle function places these one randomly
    #x = np.array(a, dtype = bool) you do not need this
    A = np.mod(np.random.permutation(m*n).reshape(m,n),2) # random bianry matrix  
    u = np.dot(A,x)# the product of A and x
    y = [1 if i > 0  else i for i in u]  #turning y into 0,1 vector
    return A, x, y # you should return all the information

def prunc(x, k):
    #This function takes a vector x and returns a vector xk with the k largest
    #in magnitude entries of x not set to zero
    indices = np.argsort(np.abs(x))[::-1]
    largest = indices[0:k]
    #print(largest)
    xk = np.zeros(len(x))
    for kl in largest:
        xk[kl] = x[kl]
    return xk


def recovery1(A,y,d,k):
    """
    to access data from the function outcome_vector
    the output is retruned in a form of a list.
    k is the number of iteration which we will stop.
    here x_0 is taken to be 0 vector
    """
    m, n = A.shape
    x_r = np.zeros(n)
    for i in range(k):
        l = np.dot(A,x_r)
        #print(l)
        v = np.array([1 if j > 0 else 0 for j in l])
        z = y-v
        b = np.dot(np.transpose(A),z)
        H = x_r + b
        x_r = H
    xbar = prunc(x_r,d)
    xbar = np.array([1 if i >0 else 0 for i in xbar])
    return xbar