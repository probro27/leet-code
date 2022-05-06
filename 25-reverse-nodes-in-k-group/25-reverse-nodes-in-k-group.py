# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def lengthList(self, head: Optional[ListNode]) -> int:
        length = 0
        while head:
            length += 1
            head = head.next
        return length
    
    def reverseList(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        prev = None
        temp = None
        while(k != 0):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            k -= 1
        lst = prev
        while lst.next:
            lst = lst.next
        lst.next = curr
        # print(prev)
        return prev
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        length = self.lengthList(curr)
        if k == 1:
            return head
        curr = self.reverseList(curr, k)
        head = curr
        num = k
        while num != 1:
            curr = curr.next
            num -= 1
        last = curr
        curr = curr.next
        length = length - k
        while length >= k and curr:
            curr = self.reverseList(curr, k)
            last.next = curr
            num = k
            while num != 1:
                curr = curr.next
                num -= 1
            last = curr
            curr = curr.next
            length = length - k
            # print(last)
        return head