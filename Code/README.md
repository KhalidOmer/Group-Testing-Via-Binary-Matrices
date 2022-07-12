# Introduction
This is a collection of code and writing that I recently worked on with Dr. Abdoelnaseer Dagoot. The work is on the Group Testing problem. The problem is minimize the number of testing required to test a community of Covid 19. 

If consider the system $Ax = y$ with A representing the measurement matrix, x being the individuals infected and y the outcome of the measurment. The problem is recover $x$ from the knowledge of $A$ and $y$. 

# Hard thresholding algorithms

the algorithm is of the form: 

# The basic iterative hard thresholding algorithm
$x^{n+1} = H_s(x^n + A^{T} * (y - A*x^{n}) $

H_n is a non-linear function that sets all non-positve values to zero.  

# The Normalised iterative thresholding algorithm
$x^{n+1} = H_s(x^n + \delta * A^{T} * (y - (A*x^{n}))$

# Binary Iteraitve Hardthresholding algorihtm

$x^{n+1} = H_s(x^n + \delta * A^{T} * (y - sign(A*x^{n}))$

# Notes 

1- $\delta$ is the stepsize or the gradiant descent 
2- sign is an operator that takes the values less than 
1 and sets them to -1 and sets them to 1 otherwise. 
3- H is an operator that keeps d largest values of x and 
sets the rest to zero. 


