'''
1. Two Sum Problem
Question: Given a list of integers and a target sum, find two distinct elements in the list that add up to the target sum.
Explanation: You need to identify two numbers in the list that, when added together, equal the given target sum.
Sample Input: [2, 7, 11, 15], target = 9
Sample Output: [0, 1] (since 2 + 7 = 9)
Complexity: 
O(n) using a dictionary

'''

def two_sum(arr,k):
    seen = set()
    for i in arr:
        if k-i in seen:
            return True
        seen.add(i)
    
    return seen


arr = [2,1,5,4,3]
k = 8

x = two_sum(arr,k)
print(x)