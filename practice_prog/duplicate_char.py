def duplicate_char_print(s):
    count = {}
    for ch in s:
        count[ch] = count.get(ch,0) + 1

    printed = set()
    for ch in s:
        if count[ch] > 1 and ch not in printed:
            print(ch)
            printed.add(ch)

s = "programming"
duplicate_char_print(s)
