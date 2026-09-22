def subarraysum(nums, k):
    count = 0
    prefix_sum = 0
    prefix_cnt = {0:1}
    
    for num in nums:
        prefix_sum += num
        
        if prefix_sum - k in prefix_cnt:
            count += prefix_cnt[prefix_sum-k]
            print("inside if ",prefix_sum-k,num)
        
        prefix_cnt[prefix_sum] = prefix_cnt.get(prefix_sum, 0) + 1
        print("prefix_sum",prefix_sum,"prefix_cnt",prefix_cnt,"count",count)
        
    print(prefix_cnt)
    print(prefix_sum)
    return count

nums = [1,2,3]
k = 3
print(subarraysum(nums,k))
