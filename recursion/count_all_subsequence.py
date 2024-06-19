arr = [4,1,3]
n = len(arr)

def func(ind=0):
    if ind >= n:
        return 1

    l = func(ind+1)
    r = func(ind+1)
    return l+r

x = func()
print(x)