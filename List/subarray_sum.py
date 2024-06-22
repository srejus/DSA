'''
Subarray Sum Equals K
Question: Given a list of integers and an integer k, find the total number of continuous 
subarrays whose sum equals to k.
Explanation: Count all subarrays that sum to k.
Sample Input: [1, 1, 1], k = 2
Sample Output: 2 (subarrays [1, 1] and [1, 1])
Complexity: 
O(n)


'''

def subarray_sum(nums,k):
    cs = 0 # cumulative_sum
    sum_count = {0:1}
    tc = 0 # total_count

    for num in nums:
        cs += num
        if cs - k in sum_count:
            tc += sum_count[cs - k]
        
        if cs in sum_count:
            sum_count[cs] += 1
        else:
            sum_count[cs] = 1
    
    return tc



nums = [1, 1, 1]
k = 2
print(subarray_sum(nums, k))
