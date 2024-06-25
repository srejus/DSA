'''
Given a sorted array and a target value v if v exist then return the index just like we return in binary search. 
If not found return the index where it would be if it were inserted in order
'''

def find_position(arr,v):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left+right) // 2
        if v == arr[mid]:
            return mid
        if v < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    
    return left