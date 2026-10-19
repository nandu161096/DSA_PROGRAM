def compress_string_cont(s):
    if not s:
        return ""

    comp_str = []
    count = 1
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            comp_str.append(s[i-1])
            comp_str.append(str(count))
            count = 1

    comp_str.append(str[-1])
    comp_str.append(str(count))
    return ''.join(comp_str)

def compress_string(s):
    cnt = {}
    comp_str = []

    for ch in s:
        cnt[ch] = cnt.get(ch,0) + 1        

    for key,val in cnt.items():
        print(key,val)
        comp_str.append(key)
        comp_str.append(str(val))

    return ''.join(comp_str)

s = "aaabbc"
print(compress_string(s))
