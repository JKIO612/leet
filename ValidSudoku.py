class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            visited = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in visited:
                    return False
                else:
                    visited.add(board[i][j])

        for c in range(9):
            visited = set()
            for d in range(9):
                if board[d][c] == ".":
                    continue
                elif board[d][c] in visited:
                    return False
                else:
                    visited.add(board[d][c])

        for x in range(9):
            visited = set()
            for y in range(3):
                for z in range(3):
                    row = (x//3) * 3 + y
                    col = (x % 3) * 3 + z
                    if board[row][col] == ".":
                        continue
                    elif board[row][col] in visited:
                        return False
                    else:
                        visited.add(board[row][col])

        return True