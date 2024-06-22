'''
inp = [1,2,3]
out = [3,2,1]

O(n) - space
O(1) - time

'''

def rev_list(arr):
    left = 0
    right = len(arr)-1

    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        left += 1
        right -= 1
    
    return arr


arr = [1,2,3]
print(rev_list(arr))