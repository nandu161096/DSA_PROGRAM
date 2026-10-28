def is_pal(s):
    sl = s.lower()
    slr = sl.replace(" ","")
    pal_str = []
    for ch in slr:
        if ch.isalpha():
            pal_str.append(ch)

    pal_str = "".join(pal_str)
    print(pal_str)
    left = 0
    right = len(pal_str) - 1
    while left < right:
        if pal_str[left] != pal_str[right]:
            return False
        left += 1
        right -=1 

    return True

s = "A man, a plan, a canal: Panama"
print(is_pal(s))
