# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        odd_list = head
        even_list = head.next
        if even_list == None:
            return head
        odd_node = odd_list
        even_node = even_list
        prev_odd = None
        prev_even = None
        while odd_node != None or even_node != None:
            if odd_node != None:
                prev_odd = odd_node
                odd_node = odd_node.next
                if odd_node != None:
                    odd_node = odd_node.next
                    prev_odd.next = odd_node
            if even_node != None:
                prev_even = even_node
                even_node = even_node.next
                if even_node != None:
                    even_node = even_node.next
                    prev_even.next = even_node
        if prev_odd != None:
            prev_odd.next = even_list
            head = odd_list
        return head

