def permutation(s):
    if len(s) == 0:
        return ['']

    perm_list = []
    for i in range(len(s)):
        part = s[:i] + s[i+1:]
        for  p in permutation(part):
            perm_list.append(s[i]+p)

    return perm_list



res = permutation("abc")
print(res)
