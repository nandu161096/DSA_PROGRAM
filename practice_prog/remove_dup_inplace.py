def remove_dup(nums):
    k = 1
    start_elt = nums[0]
    for i in range(1,len(nums)):
        print(start_elt, nums[i], i,len(nums))
        if start_elt != nums[i]:
            nums[k] = nums[i] 
            k += 1
            start_elt = nums[i]
    
    print(nums, k)

def remove_dup1(nums):
    k = 1
    start_elt = nums[0]
    for i in range(1,len(nums)):
        if nums[i] != nums[i-1]:
            nums[k] = nums[i]
            k += 1

    print(nums, k)

nums = [1, 1, 2, 2, 3]
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
remove_dup1(nums)

