class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        maximumSquareSize = min(rows, cols)
        
        additiveTable = [[0 for _ in range(cols)] for _ in range(rows)]

        additiveTable[0][0] = matrix[0][0]

        for j in range(1, cols):
            additiveTable[0][j] = additiveTable[0][j - 1] + matrix[0][j]
            
        for i in range(1, rows):
            additiveTable[i][0] = additiveTable[i - 1][0] + matrix[i][0]

        for i in range(1, rows):
            for j in range(1, cols):
                additiveTable[i][j] = additiveTable[i - 1][j] + additiveTable[i][j - 1] - additiveTable[i - 1][j - 1] + matrix[i][j]
        
        count = additiveTable[-1][-1]

        for k in range(2, maximumSquareSize + 1):
            for i in range(rows - k + 1):
                for j in range(cols - k + 1):
                    if i == 0 and j == 0:
                        window_sum = additiveTable[i + k - 1][j + k - 1]
                    elif i == 0:
                        window_sum = additiveTable[i + k - 1][j + k - 1] - additiveTable[i + k - 1][j - 1]
                    elif j == 0:
                        window_sum = additiveTable[i + k - 1][j + k - 1] - additiveTable[i - 1][j + k - 1]
                    else:
                        window_sum = additiveTable[i + k - 1][j + k - 1] - additiveTable[i + k - 1][j - 1] - additiveTable[i - 1][j + k - 1] + additiveTable[i - 1][j - 1]
                    
                    if window_sum == (k ** 2):
                        count += 1
        
        return count
                