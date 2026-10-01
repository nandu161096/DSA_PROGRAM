def nextgreater(nums):
    result = [-1] * len(nums)
    stack = []

    for i, num in enumerate(nums):
        while stack and num > nums[stack[-1]]:
            index = stack.pop()
            result[index] = nums[i]

        stack.append(i)

    return result

nums = [2,1,2,4,3]
print(nextgreater(nums))
