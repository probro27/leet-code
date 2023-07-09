class ListNode:
    val: int
    next: Optional[ListNode]
    
    def __init__(self, val: int, next: Optional[ListNode]):
        self.val = val
        self.next = next

class RecentCounter:
    queue: Optional[ListNode]

    def __init__(self):
        self.queue = None

    def ping(self, t: int) -> int:
        self.queue = ListNode(t, self.queue)
        current_node = self.queue
        prev_node = None
        number_of_nodes = 0
        while current_node and current_node.val >= t - 3000:
            number_of_nodes += 1
            prev_node = current_node
            current_node = current_node.next
        if current_node is not None:
            prev_node.next = None
        return number_of_nodes
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)