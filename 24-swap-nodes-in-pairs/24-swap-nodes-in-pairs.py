# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = head
        while lst:
            if lst.next == None:
                break
            else:
                temp = lst.val
                lst.val = (lst.next).val
                (lst.next.val) = temp
                lst = (lst.next).next
        return head