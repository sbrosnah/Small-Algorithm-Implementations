'''
Description: We need to find the longest possible subsequence of an input list. This subsequence doesn't need to be contiguous, but all members of output list 
must be in increasing order. 

ex. [5, 2, 8, 6, 3, 6, 9, 7] should output [2, 3, 6, 9] which has a length of 4. 

How to solve:
Visualize:
We can draw all the numbers as nodes and then draw edges from each node to all the possible paths that could be taken from it. We do this for every node. Now our problem is simply finding the longest path. 
Notice that this graph is a dag. The dag is already linearized for us. 

Determine Property Met: There is an ordering of subproblems (linearization of a dag) and a relation that shows how to solve a subproblem given the anser to "smaller" sub-problems.

This is a dynamic programming problem. Because we need to find the max increasing subsequence, we can split this up into subproblems each of which can be solved by the previous.

What are our sub-problems?

Our collection of subproblems is as follows: 
{L(j) : 1 <= j <= n}
meaning we need to find the length of the maximum subsequence up to node j for every node j in the list. 

What is our relation?
L(j) = 1 + max{L(i): (i, j) in E}

Now how do we do this? 
We need to find the predecessor with the maximum value, add one to that value and then put the result as the value for our current node. 
At each node, we need to the the predecessors. 
We can iterate through the list and build a graph as an adjacency list. We can then reverse the graph which takes O(n^2) time for both steps in the worst case (if there is a sequence with only increasing numbers)

Now that we know the predecessors for each node, finding L(j) is proportional to the in-degree of j (length of it's adjacency list).

We keep a length dictionary and a prev dictionary (to find the optimal solution)
'''

def longest_increasing_subsequence(arr):
    length_dict = {}
    prev_dict = {}
    graph = {}
    solution = []
    overall_max = 0
    overall_max_ind = len(arr) #this is out of bounds on purpose

    '''
    Description: create the reverse adjacency-list graph. We do this by checking if the start node of the iteration is less than the other following nodes. If so, then we add the start node to the adjacency-
    list of the current node. The length of each adjacency list is it's in-degree and each adjacency list tells us which nodes point to it in the normal (non-reversed) graph. 

    time complexity: O(n^2) 
        - We have a double for loop to find all the incoming edges of each particular node
    space complexity: O(n^2) worst case
        - each node is stored in the graph, and the first node can have at most n-1 edges
    '''
    for i in range(len(arr)):
        for j in range(i, len(arr)):

            if j not in graph:
                graph[j] = []

            if arr[i] < arr[j]:
                graph[j].append(i)
    
    '''
    Description: At each node, we check the predecessors in the length table and find the max. We set the value of the current node to the max val plus 1

    time complexity: O(n^2) worst case
        - if the entire list is in sequential order
    space complexity: O(n)
        - we populate the distance and prev dictionaries with the indices
    '''
    #for each vertex of the dag
    for i in range(len(arr)):
        max_length = 0
        max_ind = None
        #find the max length and index of all incoming edges. 
        for j in range(len(graph[i])):
            if length_dict[graph[i][j]] > max_length:
                max_length = length_dict[graph[i][j]]
                max_ind = graph[i][j]
        #The length of the current dict is equal to 1 + the max length of all the nodes that point to it
        length_dict[i] = 1 + max_length
        prev_dict[i] = max_ind
        #we keep track of the max overall length and it's index
        if length_dict[i] > overall_max:
            overall_max = length_dict[i] 
            overall_max_ind = i

    
    '''
    Description: We find the optimal solution by looping through the prev_dict

    time complexity: O(n)
        - in a linear sequence, we have n numbers in our solution
    space complexity: O(n)
        - for the same reasons as the time complexity
    '''

    #account for edge case where input array is empty
    if overall_max_ind >= len(arr): #then we know we never found a max ind because it's out of bounds
        return solution
    
    curr_ind = overall_max_ind
    while curr_ind != None:
        solution.insert(0, arr[curr_ind]) #this is a constant time operation in python
        curr_ind = prev_dict[curr_ind]
    
    return solution

def run_test(test_input):
    test_output = longest_increasing_subsequence(test_input)
    print("Test Results: ", test_output)
    print("Results Length: ", len(test_output))


if __name__=="__main__":
    test_input = [5, 2, 8, 6, 3, 6, 9, 7]
    run_test(test_input)

    test_input = [1, 2, 3, 4, 5]
    run_test(test_input)

    test_input = [5, 4, 3, 2, 1]
    run_test(test_input)

    test_input = [1, 1, 1, 1, 1]
    run_test(test_input)
