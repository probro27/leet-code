class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first_zero_index = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[first_zero_index] = nums[i]
                first_zero_index += 1
        for i in range(first_zero_index, len(nums)):
            nums[i] = 0