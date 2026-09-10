def max_contig_arr(arr):
    max_sum = float('-inf')
    curr_sum = 0
    start = end = temp_start = 0

    for i in range(len(arr)):
        curr_sum = curr_sum + arr[i]

        if curr_sum > max_sum:
            max_sum = curr_sum
            start = temp_start
            end = i

        if curr_sum < 0:
            curr_sum = 0
            temp_start = i + 1
    
    print("Maximum Sum:", max_sum)
    print("Maximum Subarray:", arr[start:end + 1])

#arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
arr = [-2, -1, -3, -4, -1, -2, -1, -5, -4, 0,1]
print(max_contig_arr(arr))
