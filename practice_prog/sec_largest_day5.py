def sec_dist_largest(arr):
    sort_arr = sorted(arr)
    largest = sort_arr[-1]
    for i in range(len(arr)-2, -1, -1):
        if sort_arr[i] != largest:
            return sort_arr[i]


arr = [10, 5, 8, 10, 3, 7]
print(sec_dist_largest(arr))
