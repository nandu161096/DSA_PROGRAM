def productExceptSelf(nums):
    n = len(nums)
    prefix = [1] * n 
    suffix = [1] * n
    final  = [1] * n
    print(n)

    for i in range(1,n):
        prefix[i] =  prefix[i-1] * nums[i-1]

    for i in range(n-2,-1,-1):
        suffix[i] =  suffix[i+1] * nums[i+1]

    for i in range(0,n):
        final[i] = prefix[i] * suffix[i]

    print("prefix",prefix)
    print("suffix",suffix)
    
    return final

nums = [1, 2, 3, 4]
print(nums)
print(productExceptSelf(nums))
