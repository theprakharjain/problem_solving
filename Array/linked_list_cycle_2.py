# Linked List Cycle II - 142- Leetcode-Medium

# Solution-1 ------------------------------------------- [Based on Floyd Cycle detection algorithm - One linked list is iterated faster than the other and both the linked list eventually meet at a certain point if any cycle exists]

slow = head
fast = head

while fast and fast.next:

    fast = fast.next.next
    slow = slow.next
    if fast == slow:
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast

return None

# Solution-2 ------------------------------------------- [Might work on real case scenerio, cant run this code on leetcode as it needs a pointer in the output instead of the value]


ptr = head
thisdict = {}
thatdict = {}
index = 0

while ptr:
    if not thisdict:
        thisdict.update({ptr: ptr})
        thatdict.update({ptr: index})
        index += 1
    if ptr != thisdict.get(ptr):
        thisdict.update({ptr: ptr})
        thatdict.update({ptr: index})
        ptr = ptr.next
        index += 1
    else:
        return thatdict.get(ptr)

return None
