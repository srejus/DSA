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

'''

Example 1
    Input: [1, 2, 3], 
    𝑘
    =
    3
    k=3

    Output: 2

    Explanation:

    Subarrays that sum to 
    3
    3 are [1, 2] and [3].
    Therefore, the output is 2.
    Example 2
    Input: [1, 1, 1, 1], 
    𝑘
    =
    2
    k=2

    Output: 3

    Explanation:

    Subarrays that sum to 
    2
    2 are [1, 1], [1, 1], and [1, 1] (considering different starting points).
    Therefore, the output is 3.
    Example 3
    Input: [1, 2, 1, 2, 1], 
    𝑘
    =
    3
    k=3

    Output: 4

    Explanation:

    Subarrays that sum to 
    3
    3 are [1, 2], [2, 1], [1, 2], and [2, 1].
    Therefore, the output is 4.
    Example 4
    Input: [-1, -1, 1, 1], 
    𝑘
    =
    0
    k=0

    Output: 4

    Explanation:

    Subarrays that sum to 
    0
    0 are [-1, 1], [1, -1], [-1, -1, 1, 1], and [-1, -1, 1, 1].
    Therefore, the output is 4.
    Example 5
    Input: [1, -1, 1, -1, 1], 
    𝑘
    =
    0
    k=0

    Output: 5

    Explanation:

    Subarrays that sum to 
    0
    0 are [1, -1], [-1, 1], [1, -1], [1, -1, 1, -1], and [1, -1, 1, -1, 1].
    Therefore, the output is 5.


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
