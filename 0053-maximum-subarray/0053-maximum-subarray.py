class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max, max_till_now = -inf, -inf
        for element in nums:
            curr_max = max(element + curr_max, element)
            max_till_now = max(curr_max, max_till_now)
        return max_till_now