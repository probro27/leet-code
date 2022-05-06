# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        prev = None
        temp = None
        while k >= 0:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            k = k - 1
        # print(prev)
        lst = prev
        while lst.next:
            lst = lst.next
        lst.next = curr
        # print(prev)
        return prev
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        low = left
        curr = head
        while low > 2:
            curr = curr.next
            low = low - 1
        last = curr
        if left != 1:
            curr = curr.next
        curr = self.reverseList(curr, right - left)
        # print(curr)
        if left != 1:
            # print(left)
            last.next = curr
        else:
            head = curr
        return head