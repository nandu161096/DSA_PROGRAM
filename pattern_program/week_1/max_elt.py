def max_elt(nums):
    max_value = 0
    for num in nums:
        if num > max_value:
            max_value = num
    return max_value

nums = [3,7,2,9,5]
print(max_elt(nums))
