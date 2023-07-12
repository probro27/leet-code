# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow_pointer = head
        fast_pointer = head

        while fast_pointer.next is not None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next
            if fast_pointer.next is not None:
                fast_pointer = fast_pointer.next
        
        right_root = slow_pointer
        
        def reverse(root: ListNode) -> ListNode:
            print(root.val)
            current = root
            previous = None
            while current is not None:
                next = current.next
                current.next = previous
                previous = current
                current = next
            root = previous
            return root
        
        right_root = reverse(right_root)
        print(right_root.val)
        max_sum = 0
        first_pointer = head
        second_pointer = right_root
        while second_pointer is not None:
            current_sum = first_pointer.val + second_pointer.val
            if current_sum > max_sum:
                max_sum = current_sum
            first_pointer = first_pointer.next
            second_pointer = second_pointer.next
        return max_sum
        
        