def missing_num(arr):
    n = len(arr)
    exp_sum = (n *(n+1))/2
    act_sum = sum(arr)
    return exp_sum - act_sum

arr = [3, 0, 1]
print(missing_num(arr))
