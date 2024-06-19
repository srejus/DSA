def func(s):
    if len(s) <= 1:
        return s

    i = 0 
    n = len(s)
    new_s = []

    while i < n:
        if i < n-1 and s[i] == s[i+1]:
            while i < n-1 and s[i] == s[i+1]:
                i += 1
        else:
            new_s.append(s[i])
        
        i += 1
    
    new_s = ''.join(new_s)
    if s == new_s:
        return s
    
    return func(new_s)


x = func("hello")
y = func("abba")

print(x)
print(y)