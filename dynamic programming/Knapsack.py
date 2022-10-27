'''
Description:
We want to find the optimal value with weight as a constraint. 
We can have with or without repetition. 

base cases:
bag holds nothing - value is nothing

K(0) = 0

Our nodes are going to be the different possible weights. We use optimal solutions for solving the current one. 

for w = 1 to W:
    K(w) = max{K(w - wi) + vi : wi <= w}
    otimal value 
'''