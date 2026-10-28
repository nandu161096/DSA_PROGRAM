def maxavgsubarr(nums, k):
    if not nums or k > len(nums):
        return None

    sum1 = 0
    for i in range(k):
        sum1 += nums[i]
    max_avg = sum1/k
    curr_avg = 0
    print("length is",len(nums))
    for i in range(len(nums)):
        print(i)

    for i in range(0,len(nums)-k):
        sum1 = sum1 - nums[i] + nums[i+k]
        curr_avg = sum1/k
        max_avg = max(max_avg, curr_avg)

    print(max_avg)

nums = [1, 12, -5, -6, 50, 3]
k = 4
maxavgsubarr(nums,k)
