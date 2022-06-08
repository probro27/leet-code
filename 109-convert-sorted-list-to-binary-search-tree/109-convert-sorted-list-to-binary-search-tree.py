# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def convertToArray(self, head: Optional[ListNode], lst: List[int]) -> List[int]:
        if not head:
            return lst
        
        else:
            lst.append(head.val)
            return self.convertToArray(head.next, lst)
        
    def sortedArrayToBST(self, lst: List[int]) -> Optional[TreeNode]:
        if lst == []:
            return None
        
        mid = len(lst) // 2
        root = TreeNode(lst[mid])
        root.left = self.sortedArrayToBST(lst[0:mid])
        root.right = self.sortedArrayToBST(lst[mid + 1:])
        
        return root
    
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        lst = self.convertToArray(head, [])
        print(lst)
        return self.sortedArrayToBST(lst)