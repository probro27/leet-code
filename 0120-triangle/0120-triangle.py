class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        dpTable = [[float("inf") for _ in triangle[-1] ] for _ in triangle]
        n = len(triangle)
        dpTable[0][0] = triangle[0][0]

        for i, row in enumerate(triangle):
            for j, col in enumerate(triangle[i]):
                if i > 0:
                    minPath = min(dpTable[i - 1][j], dpTable[i - 1][j - 1]) if j > 0 else dpTable[i - 1][j]
                    minPath = minPath + triangle[i][j]
                    dpTable[i][j] = minPath
        
        minValue = float("inf")
        for val in dpTable[n - 1]:
            if not math.isinf(val):
                minValue = min(minValue, val)
        return minValue
