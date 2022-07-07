import numpy as np
def outcome_vector(m,n,d):
    a = np.zeros(n)#Here we generate zeros
    a[:d] = 1 #turn some of zeros into ones, the portion is specified by d  
    np.random.shuffle(a) # the shuffle function places these one randomly
    x = np.array(a, dtype = bool)
    #print x
    A = []
    for i in range(m): #we use that same techniques above to generate the colmuns of A
        z=[]
        k = np.zeros(n)
        k[:d] = 1
        np.random.shuffle(k)
        z.append(k)
        A.append(z)
        #print A
    u = np.array(A, dtype = bool) #u here to assure that A is a binary matrix
    #print(u)
    y = 1*np.dot(u,x) #the one infront turns the results into 0,1 vector instead of true-false
    
    return y