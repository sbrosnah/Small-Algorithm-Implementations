
'''
Description: This function finds the maximum contiguous subarray

Time complexity: O(n)
    - The list is being iterated through one time initially. 
    - When we are building the subarray in the while loop, we will go through at most n iterations
    - This means we go through our list at most 2n times which is O(n) time. 
    - I am assuming that the insert into the front of the list is constant O(1) time. 
Space complexity: O(n)
    - I could probably use less space, but it doesn't matter because the worst case space complexity is going to be O(n) anyways because we are have to return the 
    contiguous subarray which could be the whole array in the worst case. 
    - I use a totals array, a prev array, and a return value array which has a space complexity of 3n = O(n) 
'''
def MaxContigSub(arr):
    totals = []
    prev = []
    curr_max = 0 #This will always at least be zero
    best_max = 0 #our best_max will never be negative and an empty array max sum is 0
    max_ind = len(arr) #This is out of range

    for i in range(len(arr)):

        if i > 0 and totals[i - 1] > 0:
            prev.append(i - 1)
        else:
            prev.append(None)

        if arr[i] + curr_max > 0:
            curr_max += arr[i]
            totals.append(curr_max)
        else:
            totals.append(0)

        if totals[i] > best_max:
            best_max = curr_max
            max_ind = i
    
    ret_val = []

    if max_ind == len(arr):
        return ret_val

    curr_ind = max_ind
    while curr_ind != None:
        ret_val.insert(0, arr[curr_ind])
        curr_ind = prev[curr_ind]

    return ret_val

if __name__=="__main__":
    test = [-1, 1, 2, 3, -1, -1, -1, 5]
    result = MaxContigSub(test) 
    print("Resulting array: ", result) 
    print("Resulting sum: ", sum(result))

    test = [1, 2, 3, -10, 1, 2, 3, -1, -1, -1, 5]
    result = MaxContigSub(test)   
    print("Resulting array: ", result)
    print("Resulting sum: ", sum(result))

    test = [-5, -5, -5]
    result = MaxContigSub(test)   
    print("Resulting array: ", result)
    print("Resulting sum: ", sum(result))

    test = [0, 0, 0, 0]
    result = MaxContigSub(test)   
    print("Resulting array: ", result)
    print("Resulting sum: ", sum(result))

    test = [0, 0, 0, 0, 1]
    result = MaxContigSub(test)   
    print("Resulting array: ", result)
    print("Resulting sum: ", sum(result))
