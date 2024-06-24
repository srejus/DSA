'''
We can solve this in 2 ways

1. using seen set
2. using 2 pointers slow/fast

Complexities

Time
O(n) for both

Space
O(n) for 1st
O(1) for 2nd

'''

# second solution / two pointer solution

def has_cycle(head):
    slow = head
    fast = head.next

    while fast and fast.next:
        if fast == slow:
            return True
        
        fast = fast.next.next
        slow = slow.next
    
    return False


# first solution using set/hashmap

def has_cycle_1(head):
    seen = set()
    curr = head
    while curr:
        if curr in seen:
            return True
        
        seen.add(curr)
        curr = curr.next
    
    return False