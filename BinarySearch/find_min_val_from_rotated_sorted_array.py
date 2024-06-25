def find_min(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left+right) // 2

        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid
    
    return arr[right]


arr = [7,8,9,2,3,4]
x = find_min(arr)
print(x)

# ans : 2 - > two is the smallest value here