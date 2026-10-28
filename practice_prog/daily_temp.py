def daily_temp(tempe):
    stack = []
    answer = [0] * len(tempe)

    for i in range(len(tempe)):

        while stack and tempe[i] > tempe[stack[-1]]:
            prev_index = stack.pop()
            answer[prev_index] = i-prev_index

        stack.append(i)

    return answer

temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(daily_temp(temperatures))
