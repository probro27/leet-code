from typing import (
    List,
)

class Solution:
    """
    @param heights: An integer array
    @return: Indexs of buildings with sea view
    """
    def find_buildings(self, heights: List[int]) -> List[int]:
        currentTallest = 0
        buildings_with_view = []

        for index, height in enumerate(heights[::-1]):
            actualIndex = len(heights) - index - 1
            if height > currentTallest:
                buildings_with_view.append(actualIndex)
                currentTallest = height
        
        return buildings_with_view[::-1]
