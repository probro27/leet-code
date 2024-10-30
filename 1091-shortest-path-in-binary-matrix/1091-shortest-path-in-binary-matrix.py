class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        
        n = len(grid)
        queue = deque([((0, 0), 1)])  # Queue stores (position, path_length)
        visited = set([(0, 0)])
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        while queue:
            (x, y), path_length = queue.popleft()
            
            if (x, y) == (n - 1, n - 1):  # Reached the target
                return path_length
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append(((nx, ny), path_length + 1))
        
        return -1  # Target not reachable