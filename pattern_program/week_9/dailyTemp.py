def daily_temp(tempe):
    n = len(tempe)
    answer = [0] *n
    stack = []

    for i, temp in enumerate(tempe):
        if stack:
            print("Stack at beginning",
                  stack,
                  "index", i,
                  "temp", temp,
                  "top", stack[-1],
                  tempe[stack[-1]])
        else:
            print("Stack at beginning",
          stack,
          "index", i,
          "temp", temp,
          "stack is empty")

        while stack and temp > tempe[stack[-1]]:
            prev_index = stack.pop()
            answer[prev_index] = i - prev_index

        stack.append(i)
        print("Stack at the end of for loop",stack,"index",i,"temp",temp,"top of stack",stack[-1],tempe[stack[-1]])

    return answer

temperatures = [73,74,75,71,69,72,76,73]
print(daily_temp(temperatures))
temperatures = [74,72,71,70,69,78]
print(daily_temp(temperatures))
