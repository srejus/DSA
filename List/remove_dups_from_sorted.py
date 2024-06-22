'''
Remove duplicate element from sorted array of integers

O(n)

'''

def remove_duplicates(arr):
    if not arr:
        return arr
    
    i = 0
    for j in range(1,len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
    
    return arr[:i+1]



arr = [1,2,2,3,4,4,5]
x = remove_duplicates(arr)
print(x)