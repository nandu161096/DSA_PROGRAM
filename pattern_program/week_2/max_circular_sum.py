def max_contig_circ_arr(arr):
    max_sum = float('-inf')
    curr_sum = 0

# for max sum
    for num in arr:
        curr_sum = curr_sum + num

        if curr_sum > max_sum:
            max_sum = curr_sum

        if curr_sum < 0:
            curr_sum = 0

#for min sum
    min_sum = float('inf')
    curr_min = 0
    for num in arr:
        curr_min = curr_min + num

        if curr_min < min_sum:
            min_sum = curr_min

        if curr_min > 0:
            curr_min = 0

    total_sum = sum(arr)

    if max_sum < 0:
        return max_sum

    circ_sum = total_sum - min_sum
    return max(circ_sum, max_sum)

arr = [-2, -1, -3, -4, -1, -2, -1, -5, -4, 0,1]
print(max_contig_circ_arr(arr))
arr = [5, -3, 5]
print(max_contig_circ_arr(arr))
