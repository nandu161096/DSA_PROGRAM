def isValid(s):
    stack = []
    pairs = {'}':'{',']':'[',')':'('}
    for ch in s:
        if ch in pairs.values():
            stack.append(ch)
        else:
            if not stack:
 #               print("Not valid in if case",stack)
                break
            if stack[-1] != pairs[ch]:
#                print("Not valid in sec if ",stack,s)
                break
            stack.pop()

    if len(stack) == 0:
        print("Valid")
    else:
        print("Not valid")



s = "()[]{}"
isValid(s)
s = "([{}])"
isValid(s)
s = "(]"
isValid(s)

