'''
Time: O(log(n))
Space: O(1)
'''


def binary_search(arr,v):
    left = 0
    right = len(arr)-1

    while left <= right:
        mid = (left+right)//2
        if v == arr[mid]:
            return mid
        if v < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    
    return -1



arr = [1,2,3,4,5,7,10,12,15]
v = 7

x = binary_search(arr,v)
print(x)
