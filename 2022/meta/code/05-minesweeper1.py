import random


class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        m = len(board)
        n = len(board[0])
        moves = {(0,1),(0, -1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)}

        def inBound(r,c):
            return 0 <= r < m and 0 <=c<n

        def dfs(r,c):
            '''If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
            '''
            if not inBound(r,c)or board[r][c] == 'M':
                return 
            
            mines = 0
            # calc mine count
            for move in moves:
                next_r = r + move[0]
                next_c = c + move[1]
                if inBound(next_r,next_c) and board[next_r][next_c] == 'M':
                    mines +=1
            """If an empty square 'E' with no adjacent mines is revealed, then change it to a revealed blank 'B' and all of its adjacent unrevealed squares should be revealed recursively.
"""        
            if mines == 0:
                if board[r][c] == 'E':
                    board[r][c] = 'B'
                for move in moves:
                    next_r = r + move[0]
                    next_c = c + move[1]
                    if inBound(next_r, next_c) and board[next_r][next_c] == 'E':
                        dfs(next_r,next_c)
            else:
                """If an empty square 'E' with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
"""
                if board[r][c] == 'E':
                    board[r][c] = str(mines)
        
        row , col = click[0], click[1]
        if board[row][col] == 'M':
            board[row][col] = 'X'
            dfs(0,0)
        else:
            dfs(row,col)
        return board


def generate(m, n, p):
    import random
    board = [ ['E'] * n for _ in range(m)]
    
    visited = set()
    
    while len(visited)< p:
        choosed = random.randint(0, m*n-1)
        if choosed in visited:
            continue
        else:
            visited.add(choosed)
            
    
    for mine in visited:
        print(mine//m,mine%n)
        board[mine // n][mine % n] = 'M'
    return board


if __name__ == '__main__':
    board =generate(2, 3, 3)
    print(board)
    new = Solution().updateBoard(board,(0,1))
    print(new)
