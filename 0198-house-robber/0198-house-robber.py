class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1 for _ in nums]
        def recursive(nums: List[int]) -> int:
            n = len(nums)
            if n == 0:
                return 0
            if n == 1:
                return nums[0]

            if dp[n - 2] != -1:
                exclude_res = dp[n - 2]
            else:
                exclude_res = recursive(nums[:n - 1])
                dp[n - 2] = exclude_res
            
            if n >= 3:
                if dp[n - 3] != -1:
                    include_res = dp[n - 3]
                else:
                    include_res = recursive(nums[:n - 2])
                    dp[n - 3] = include_res
            else:
                include_res = 0

            result =  max(nums[-1] + include_res, exclude_res)
            # print(f"{nums[:n - 2]}, {nums[:n - 1]}: {result}")
            dp[n - 1] = result
            return result
        
        return recursive(nums)