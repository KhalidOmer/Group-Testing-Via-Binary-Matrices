import numpy as np

"""Normalized Now we work on the matrix A, first let us pick A which satisfies:
\begin{equation}\lVert  Ax  \rVert_1 = c, \quad c>0\end{equation} For this we introduce the first norm function here we call it taxicab and then use  it in bulding the constraint c function, this function returns a matrix A which satisfies the condition above. After this we rebulid the code of the modified algorithm above. We call the function "sparse_recovery" and it takes m,n, d, c and k. Where m,n are the dimensions of the matrix A, d repsents the level of sparsity and it can be appoximated by $p * n$ where is the prevalence level of the disease, c is a constant to be chosen, and k here is the number of iteration to be performed by the algorithm."""
########################################


def taxicab(A,x):
    sum =0 
    for i in np.dot(A,x):
        a = abs(i)
        sum=sum+a
    return sum
    
#########################################    
def constraint(m,n,d,c,x):
    while True:
        A = np.mod(np.random.permutation(m*n).reshape(m,n),2)
        if taxicab(A,x) > c:
            A = np.mod(np.random.permutation(m*n).reshape(m,n),2)
        else:
            break
    return A   
    
#########################################    
def sparse_recovery(m,n,d,c,k):
      """The implementaion of the normalized hard thresholding algorithm.
      ----------------------------
      Parameters: 
      ---------
      ->m,n are the testing matrix A dimensions
      ->d represents the level of sparsity as it is approximated by the prvalence 
      rate and the size of the vector x, d = p*n
      ->c is a constant that is positive and chosen conveniently
      ->k is the number of iterations to be performed, here it is taken 
      as a stoping ceriterion
      Structure: 
      ----------  
      the constraint function applies the first norm constraint, 
      q is the step size """
      x = np.zeros(n)#Here we generate zeros
      x[:d] = 1 #turn some of zeros into ones, the portion is specified by d  
      np.random.shuffle(x) #here is the vector x
      print("x = ", x)
      A = constraint(m,n,d,c,x) 
      y = np.dot(A,x)
      x_r = np.zeros(n)
      for i in range(k):
          l = np.dot(A,x_r)
          g = np.dot(np.transpose(A),(y - np.dot(A, x_r)))
          q = np.dot(np.transpose(g),g)/(np.dot(np.dot(np.transpose(g),np.transpose(A)),np.dot(A,g)))
          v = np.array([i if i > 0 else 0 for i in l])
          z = y-v
          b = np.dot(np.transpose(A),z)
          H = x_r + q * b
          x_r = H
      t = np.sort(x_r)[::-1]
      x_r = np.array([1 if i>=t[1] else 0 for i in x_r])
      return x_r
      
####################################################
