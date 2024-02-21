class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        path_to_border = [[False for _ in range(n)] for _ in range(m)]
        
        def check_current_position(position: Tuple[int, int]) -> bool:
            x, y = position
            if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                path_to_border[x][y] = True
                return False
            visited[x][y] = True
            results = [True for _ in range(4)]
            checking_positions = [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]
            for idx, pos in enumerate(checking_positions):
                posx, posy = pos
                if not visited[posx][posy] and board[posx][posy] == "O":
                    results[idx] = check_current_position((posx, posy))
                elif visited[posx][posy] and board[posx][posy] == "O" and path_to_border[posx][posy]:
                    results[idx] = False
                if results[idx] == False:
                    path_to_border[x][y] = True
                    return False
            if sum(results) == 4:
                dependencies.append((x, y))
                return True
            else:
                path_to_border[x][y] = True
                return False

        for x in range(1, m - 1):
            for y in range(1, n - 1):
                if not visited[x][y] and board[x][y] == "O":
                    dependencies = []
                    result = check_current_position((x, y))
                    if result:
                        for x1, y1 in dependencies:
                            board[x1][y1] = 'X'
