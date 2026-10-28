def two_sum(numbers, target):
    visited = {} 

    for i,num in enumerate(numbers):
        #need = target - numbers[i]
        need = target - num

        if need in visited:
            return [visited[need]+1, i+1]

        visited[num] = i
    return []

numbers = [2, 7, 11, 15]
target = 9
print(two_sum(numbers, target))
numbers = [2, 3, 4]
target = 6
print(two_sum(numbers, target))
