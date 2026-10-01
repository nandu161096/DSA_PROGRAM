from collections import deque 

def maxvalueslidingwin(nums,k):
    dq = deque()
    result = []

    for i, num in enumerate(nums):
        if dq:
            print("in start",num,nums[dq[-1]],dq[-1])
        while dq and nums[dq[-1]] < num:
            dq.pop()

        dq.append(i)
        print(dq,"i-k", i-k,"k-1",k-1,"i",i)

        if dq[0] <= i-k:
            dq.popleft()

        if i >= k-1:
            print("append occurs",dq[0], nums[dq[0]])
            result.append(nums[dq[0]])
        print(dq,result)

    return result

nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(maxvalueslidingwin(nums,k))
