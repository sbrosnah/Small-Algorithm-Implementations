#return the index of target if found in nums. Otherwise return -1
def search(nums, target):
    return search_helper(nums, target, 0, len(nums) - 1)


def search_helper(nums, target, beginning, end):
    #base cases
    if len(nums) == 0:
        return -1
    if beginning > end:
        return -1

    #round down 
    pivot = ((end - beginning) // 2) + beginning
    if nums[pivot] == target:
        return pivot
    #Because the list is sorted, if the value is less, then we know it must lie in the part above
    elif nums[pivot] < target:
        return search_helper(nums, target, pivot + 1, end)
    else:
        #Then we know that the number at pivot must be greater than target
        return search_helper(nums, target, beginning, pivot - 1)


if __name__=="__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(search(nums, target))

    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    print(search(nums, target))