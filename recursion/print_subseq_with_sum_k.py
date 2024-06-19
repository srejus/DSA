arr = [4,1,2]
n = len(arr)
k = 3

def func(ind=0,res=[],sm=0):
    if ind >= n:
        if sm == k:
            print(res)
            return True
        return False
    
    res.append(arr[ind])
    sm += arr[ind]
    if func(ind+1,res,sm) is True:
        return True
    res.pop()
    sm -= arr[ind]
    if func(ind+1,res,sm) is True:
        return True
    return False


func()