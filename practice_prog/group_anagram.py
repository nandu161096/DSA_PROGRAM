from collections import defaultdict

def group_ana(strs):
    group = defaultdict(list)

    for str1 in strs:
        key = "".join(sorted(str1))
        group[key].append(str1)

    print(group)
    return list(group.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print("\n",group_ana(strs))
