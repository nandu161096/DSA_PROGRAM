def max_profit_using_kadane(prices):
    n = len(prices)
    print(prices)
    diff = [0] * (n-1)
    for i in range(1,n):
        diff[i-1] = prices[i] - prices[i-1] 

    print(diff)

    max_sum = float('-inf')
    curr_sum = 0

    for i in range(len(diff)):
        curr_sum = curr_sum + diff[i]

        if curr_sum > max_sum:
            max_sum = curr_sum

        if curr_sum < 0:
            curr_sum = 0

#    print(max_sum)
    return max_sum

prices = [7, 1, 5, 3, 6, 4]
print(max_profit_using_kadane(prices))
