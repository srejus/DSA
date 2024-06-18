arr = [3,1,2]
n = 3

def func(idx=0,lst=[]):
    if idx >= n:
        print(lst)
        return
    
    lst.append(arr[idx])
    func(idx+1,lst)
    lst.pop()
    func(idx+1,lst)


func()