# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return head
        pos = 0
        hashmap = {}
        flag = False
        curr = head
        while curr:
            if curr in hashmap.keys():
                flag = True
                break
            else:
                hashmap[curr] = pos
                pos += 1
            curr = curr.next
        if flag:
            return True
        else:
            return False