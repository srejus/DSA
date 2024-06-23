def rotate_arr(arr,k):
    k = k % len(arr)
    
    if k == 0:
        return arr

    split_index = len(arr) - k
    rotated_ary = arr[split_index:]+arr[:split_index]
    return rotated_ary


arr = [1,2,3,4,5,6,7]
k = 3
print(rotate_arr(arr,k))