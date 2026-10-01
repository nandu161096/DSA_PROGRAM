def isValid(s):
    stack = []
    pairs = { ')' : '(', '}' : '{', ']': '['}

    for ch in s:
        if ch in pairs.values():
            stack.append(ch)
            print(stack)
        else:
            if not stack:
                return False
            if stack[-1] != pairs[ch]:
                print(stack[-1], pairs[ch], ch,stack)
                return False
            print(stack)
            stack.pop()
            print("after pop",stack)

    return len(stack) == 0

print(isValid("()[]{}")) # True
#print(isValid("(]")) # False
