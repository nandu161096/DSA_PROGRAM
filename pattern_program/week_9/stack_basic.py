stack = []

stack.append(10)
stack.append(20)
stack.append(30)

for num in stack:
    print(num)

for i in range(len(stack)):
    print(stack[i],i)

print(stack[-1], stack[-2], stack[-3])
