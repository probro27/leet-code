class Solution:

    def __init__(self, w: List[int]):
        self.total_sum = sum(w)
        self.prefixSum = []
        current_sum = 0
        for i in w:
            current_sum += i
            self.prefixSum.append(current_sum)
        self.w = w

    def pickIndex(self) -> int:
        index = random.randint(0, self.total_sum - 1)
        for idx, curr in enumerate(self.prefixSum):
            if curr > index:
                return idx
        return len(self.prefixSum) - 1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()