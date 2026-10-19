def two_sums(nums, target):

    visited = {}
    for i, num in enumerate(nums):
        need = target - nums[i]

        if need in visited:
            return [visited[need], i]
        visited[num] = i

nums = [2, 7, 11, 15]
target = 9
print(two_sums(nums,target))
