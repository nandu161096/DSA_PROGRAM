from collections import deque

def maxslidingwin(nums,k):
    result = []
    dq = deque()

    for i in range(len(nums)):
        if dq and dq[0] <= i - k:
            dq.popleft()

        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(maxslidingwin(nums,k))
