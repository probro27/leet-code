# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_fast = head.next
        current_slow = head
        prev_slow = None
        while current_fast != None:
            print(current_slow.val)
            prev_slow = current_slow
            current_slow = current_slow.next
            current_fast = current_fast.next
            if current_fast != None:
                current_fast = current_fast.next
        if prev_slow != None:
            prev_slow.next = current_slow.next
        else:
            head = None
        return head
        