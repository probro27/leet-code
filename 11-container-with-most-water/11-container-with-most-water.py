class Solution:
    def maxArea(self, height: List[int]) -> int:
        low = 0
        high = len(height) - 1
        maxArea = 0
        pillar1 = 0
        pillar2 = len(height) - 1
        
        while low < high:
            if ((high - low) * min(height[low], height[high])) > maxArea:
                maxArea = (high - low) * min(height[low], height[high])
            if height[low] < height[high]:
                low = low + 1
            else:
                high = high -1 
        
        return maxArea