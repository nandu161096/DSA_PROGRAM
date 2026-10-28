def maxslidingwin(nums,k):
    result = []
    print(nums)
    print("len of nums",len(nums))
    for i in range(len(nums) -k +1):
        result.append(max(nums[i:i+k]))

    return result

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(maxslidingwin(nums,k))
