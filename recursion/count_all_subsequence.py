arr = [4,1,3]
n = len(arr)

def func(ind=0,res=[]):
    if ind >= n:
        return 1

    res.append(arr[ind])
    l = func(ind+1,res)
    res.pop()
    r = func(ind+1,res)
    return l+r

x = func()
print(x)