def nxt_greater(nums):
    result = [-1] * len(nums)
    stack = []

    for i in range(len(nums)):
        #while stack and nums[stack[-1]] < nums[i]:
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)

    return result

nums = [4, 5, 2, 10]
print(nxt_greater(nums))
