def sortArray(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    #base case
    if len(nums) <= 1:
        return nums
    
    return merge(sortArray(nums[:len(nums) // 2]), sortArray(nums[len(nums) // 2:]))

def merge(arr1, arr2):
    #merge the sorted lists
    if len(arr1) == 0 and len(arr2) == 0:
        return []
    elif len(arr1) == 0:
        return arr2
    elif len(arr2) == 0:
        return arr1
    
    #At this point, we know that no edge cases occured
    pos1 = 0
    pos2 = 0
    new_list = []
    while True:
        #if either of the positions are none, then we can just add the rest of the other to the new lists
        if pos1 == len(arr1) and pos2 == len(arr2):
            return new_list
        elif pos1 == len(arr1):
            new_list.extend(arr2[pos2:])
            return new_list
        elif pos2 == len(arr2):
            new_list.extend(arr1[pos1:])
            return new_list

        #add the smallest of the two current elements to the lists
        if arr1[pos1] <= arr2[pos2]:
            new_list.append(arr1[pos1])
            pos1 += 1
        else:
            new_list.append(arr2[pos2])
            pos2 += 1
    


if __name__=="__main__":
    nums = [5,2,3,1]
    print(sortArray(nums))