def max_contig_arr(arr):
    res = arr[0]
    max_end = arr[0]
    for i in range(1,len(arr)):
        max_end = max(max_end+arr[i], arr[i])
        res = max(res,max_end)

    return res

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_contig_arr(arr))
