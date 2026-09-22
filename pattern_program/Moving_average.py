from collections import deque 

window = deque()
k = 3
curr_sum = 0
data = [20,25,30,40,35,50]

for value in data:
    window.append(value)
    curr_sum += value
    
    if len(window) > k:
        curr_sum -= window.popleft()
        
    if len(window) == k:
        print(curr_sum/k)
