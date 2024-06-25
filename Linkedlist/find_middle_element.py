'''
Time: O(n)
Space: O(1)
'''

def find_mid(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow.data