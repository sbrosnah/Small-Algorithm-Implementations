'''
Description: We need the minimum cost to convert one string into another. We do this by creating a matrix and solving the minumum number of edits for each substring possibility 
dynamically. We can perform 3 things. 

Consider the two starting words
THARS
OTHER

We are trying to convert the first word to the send one in the least number of moves. 

An insert (cost 1)
_THARS
OTHER

A substitute (cost 1)
_THERS
OTHER

A delete (represented as an insert in the second word) (cost 1)
_THERS
OTHER_


1. Our problem can be broken up into sub problems, but not by a reduction factor. Each sub problem differs by one letter which means that this problem is great for dynamic 
programming!

2. Visualization:
We can start small and then get larger to determine our sub-problems. If we have two blank strings, we don't need to do anything. 
-
-
They are equal, so we don't do anything

If we have a string with one character with an empty string, we just delete that character. If we have an empty string with a single character, we insert it. 
A
-
We delete A and it becomes
-
-

-
A
We insert A into the first string and it becomes
-
-

If we have two strings, each with one character each, we can see if they are equal or not. If they are, we do nothing. If they aren't, we substitude the top character for the bottom
one at that same position
A
B
switches to 
-
B

We can do this same thing for two characters compared with 0, 1, or 2 characters of the other string. We can use the best cost for the previous substring pairing solved. 
We can continue to do this up to the full two strings. We will end up populating a matrix with the minimal costs of each substring pairing starting at the top left corner and filling 
it out from left to right and down. 

3. Sub-Problem Enumeration
We know there are 3 subproblems that need to be solved at any given cell in our matrix
E(i - 1, j)
E(i, j - 1), 
E(i - 1, j - 1)
We want to consider these three sub-problems and take the one that will result in the lowest cost. 

4. There is a specific order we need to solve these subproblems in and so it can be visualized as a DAG. Therefore, we can solve this problem dyamically. As stated earlier, this 
problem needs to be solved by creating a matrix that can be solved from left to right and down so that we can consider all of the possible sub-problems and use the one that will result
in the best possible solution for any given cell. This will help give us an efficient exhaustive search of the possible solutions 

5. Recurrence Relation

E(i, j) = min{1 + E(i - 1, j), 1 + E(i, j - 1), diff(i, j) + E(i - 1, j - 1)}
note that diff just means that if i and j are different, it is adding a cost of 1. If they are the same it is a cost of 0. 

6. Implementation

I will build a 2D array whose indices line up with the indices of the strings. The columns will represent the letters in the second word which is the word that we are changing to. There will be n columns which we will index into using j
The rows will represent the letters in the first word which is the word that we are changing. There will be m rows and we will index into the rows using i. If I iterate through this matrix from left to right and down, I will be able to access 
all of the minimum costs for all the subproblems needed to determent the minimum cost of the current cell. 

We can keep a prev dictionary to show the transformations taken. However, this isn't necessary because our final answer is just the bottom-right most cell of our matrix. 

MODIFICATION!
I also want to be able to find a good solution for huge strings, but not an optimal one because enumerating all of the sub-problems takes up a huge amount of resources and computation 
time for huge strings. Because of this, we will declare a Max sub-string variable that indicates the maximum substring size considered for any given cell in our matrix. This will 
result in a diagonal strip accross the matrix that contains the cells that we solve for. The bottom-right most cell will be a good answer, but won't be the optimal one. 

Time Complexity:

Space Complexity: 

'''

import numpy as np

USE_NEEDLEMAN = True

if USE_NEEDLEMAN == False:
    INDEL = 1
    SUB = 1
    MATCH = 0
else:
    INDEL = 5
    SUB = 1
    MATCH = -3

#Tie breaking order: Left, top, diagonal

def EditDistance(strings, d = None):
    str_1 = str.lower(strings[0])
    str_2 = str.lower(strings[1])

    #Check the base cases (shortcuts to save computation)
    #This case takes care of the cases where they are both empty and when they both arent but equal
    if str_1 == str_2:
        return 0, ""
    #When one is empty and the other isn't
    if len(str_1) == 0 and len(str_2) != 0:
        #Because we will need to do that many insertions
        return len(str_2) * INDEL, str_2
    if len(str_1) != 0 and len(str_2) == 0:
        return len(str_1) * INDEL, str_1
    
    #If the d that is passed in is 0???
    
    #At this point, we now now that there is at least one row and at least one column in our matrix

    '''
    If it's not defined, we don't want to have a constraint, so we set it to the largest string length so it doesn't constrain our answer and so we don't need to change
    any of our code. 
    '''
    #These are the dimensions of our matrix. We add one for the row and col representing the empty string
    m = len(str_1) + 1
    n = len(str_2) + 1

    #This is the max possible 2d +1 value if we are not using the banded approach. We subtract one because the 
    #Null character has been added in already. 
    max_possible = max(m, n) * 2 - 1

    #we use d to determine what 
    if d == None:
        max_sub_size = max_possible
        curr_width = max_sub_size
    else:
        #The max size is this because we add 1 to a row of length d d+1 times. d + 1 because we account 
        #for the null char at the beginning of each string. 
        max_sub_size = 2 * d + 1
        curr_width = d + 1

    matrix = {}
    prev = {}

    #We keep a curr_start and curr_end index to help with our banded algorithm so that once we hit the curr_width 
    start_ind = 0

    #We now start interating through the strings to determine the costs at each cell. 
    for i in range(m):

        for j in range(start_ind, n):

            #Check our base cases for filling out the matrix. 

            # Are we past curr_width? If so, update values as needed and go to the next iteration
            #This is for while it is possible to index to the right
            if j > (start_ind + curr_width - 1) and max_sub_size < max_possible:

                #Update values as needed

      
                #If we are doing the banded algorithm (max_sub_size < n) and our curr_width is the max_sub size
                #Note that even if max_sub size is equal to the width of the input strings, it will still be smaller than
                #the actual max_possible because the actual max_possible accounts for null characters at the beginning
                #of the strings. 
                if curr_width == max_sub_size:
                    start_ind += 1

                if curr_width < max_sub_size:
                    curr_width += 1

                #skip to the next row iteration
                break

            # Are we on the first row or column? 
            if i == 0 and j == 0:
                matrix[i, j] = 0
                prev[i, j] = None
                continue
            elif i == 0:
                matrix[i, j] = j * INDEL
                #We know that j must be greater than 0 because i = 0 and we know both arent equal to 0
                prev[i, j] = (i, j - 1)
                continue
            elif j == 0: 
                matrix[i, j] = i * INDEL
                prev[i, j] = (i - 1, j)
                continue

            # At this point, we know that we aren't on the first row or column and the current 'cell' is within the constraints for the banded algorithm 
            # We still need to check left and right. However, if our current cell is in the band, your diagonal will never not be. 

            # We find all the applicable sub-problems and we put them into costs so we can find the min later
            min_cost = np.inf
            min_key = None

            #This specific order of if statements will ensure that the correct tie breaking cases are considered. 

            if j > start_ind:
                #You can find the one to the left
                #If our optimal path uses the cell to the left goes to the right, this means that we perfom an insertion on our word
                left = matrix[i, j - 1] #min cost computed for the cell to the left
                if left < min_cost:
                    min_cost = left + INDEL
                    min_key = (i, j - 1)

            if j < (start_ind + curr_width - 1) or max_sub_size == max_possible: #If equal, we aren't doing the banded
                #You can find the one above
                #If our optimal path uses the cell above in the matrix and moves down, this means that we perform a deletion on our word
                above = matrix[i - 1, j] #min cost computed for the cell above
                if above < min_cost:
                    min_cost = above + INDEL
                    min_key = (i - 1, j)

            #You can find the diagonal cell
            # If our optimal path uses the cell to the upper left (diagonal) and moves diagonally to the lower right in the matrix, this means that we either perform a substitution
            # or keep that character at that position the same. 

            #The string indexes are offset by 1
            if str_1[i - 1] == str_2[j - 1]: #This will be either a 1 or a 0 because 
                #Then it's a match
                c = MATCH
            else:
                c = SUB

            diagonal = matrix[i - 1, j - 1] + c #This will be the min cost computed for the diagonal cell
            if diagonal < min_cost:
                min_cost = diagonal
                min_key = (i - 1, j - 1)

            #Once we find the min cost, insert it into the matrix cell
            matrix[i, j] = min_cost
            #Set prev
            prev[i, j] = min_key

            #This is for while it isn't possible to index to the right so we can still shrink the start
            if j == n - 1 and max_sub_size < max_possible:
                start_ind += 1
    
    curr_cell = (m - 1, n - 1)
    output = []
    while True:
        #The first part of the cell tuple gives us the letter of the word we are changing, the second corresponds
        #to the word we are changing to. We want to insert a '-' if it was an indel, otherwise, we wantthe actual
        # letter (if we moved diagonally)
        prev_cell = prev[curr_cell]
        if prev_cell == None:
            #Then we are on the null string base case and can exit
            break

        #code goes here
        if curr_cell[0] - 1 == prev_cell[0] and curr_cell[1] - 1 == prev_cell[1]:
            #Then it was a diagonal
            #Needs to be minus one because our matrix is offset by 1
            output.insert(0, str_1[curr_cell[0] - 1])
        else:
            #It was an indel, so we store a hyphen
            output.insert(0, '-')

        curr_cell = prev_cell
    
    #Convert array tostring
    out_str = "".join(output)
        

    return matrix[m - 1, n - 1], out_str

def run_test(test_input, d = None):
    test_cost, test_str = EditDistance(test_input, d)
    print("Test Cost: ", test_cost)
    print("Test Output: ", test_str)


if __name__=="__main__":


    #Expected: 0
    test_input = ["", ""]
    run_test(test_input)

    #Expected: 1
    test_input = ["A", "B"]
    run_test(test_input)

    #Expected: 1
    test_input = ["A", ""]
    run_test(test_input)

    #Expected: 1
    test_input = ["", "B"]
    run_test(test_input)

    #Expected: 1
    test_input = ["", "B"]
    run_test(test_input)

    #Expected: 0
    test_input = ["b", "B"]
    run_test(test_input)

    #Expected: 3
    test_input = ["thars", "other"]
    run_test(test_input, 2)

    #Expected: 3
    test_input = ["Thars", "oTher"]
    run_test(test_input, 2)

    #Expected: -1
    test_input = ["exponential", "polynomial"]
    run_test(test_input)

    #Expected: -1
    test_input = ["exponential", "polynomial"]
    run_test(test_input, 2)

    #Expected: -2
    test_input = ["ATGCC", "TACGCA"]
    run_test(test_input, 2)