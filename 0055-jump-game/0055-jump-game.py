class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump_list = [False for _ in nums]
        jump_list[-1] = True
        last_index = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            can_jump = False
            for j in range(1, nums[i] + 1):
                if i + j <= last_index:
                    if jump_list[i + j]:
                        can_jump = True
                        break
                else:
                    break
            jump_list[i] = can_jump
        
        return jump_list[0]