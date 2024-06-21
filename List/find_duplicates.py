'''
3. Find Duplicates
Question: Given a list of integers, find all the elements that appear more than once.
Explanation: Identify all elements that have duplicates in the list.
Sample Input: [4, 3, 2, 7, 8, 2, 3, 1]
Sample Output: [2, 3]
Complexity: 
O(n) using a dictionary
'''

def find_duplicates(arr):
    frequency = {}
    duplicates = []

    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    for key, value in frequency.items():
        if value > 1:
            duplicates.append(key)
    
    return duplicates



arr = [2,1,5,4,2,7,9,7]

x = find_duplicates(arr)
print(x)
            