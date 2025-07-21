
def safe(board, row, col, n):
       for i in range(row):
        if board[i][col] == 'Q':
            return False\
            
            i,j= row -1,col-1
            while i>=0 and j<n:
             if board[i][j] == 'Q':
                return False        
            i -=1
            j += 1
def print_board(board):
        if board[i][col] == 'Q':
            return False    
        
        if col - (row - i) >= 0 and board[i][col - (row - i)] == 'Q':
            return False
        if col + (row - i) < n and board[i][col + (row - i)] == 'Q':
            return False
\

def solve(board, row,n):
    if row == n:
          print_board(board)
        return

for col in range(n):
        if(safe(board,row,col,n)):
            board[row][col] = 'Q'
            solve(board, row + 1, n)
            board[row][col] = '.'

            def print_board(board,y):
                 for i in range(n):
                     print("".join(i))

print()
def
for j in range(len(board)):
                         print(board[i][j], end=" ")
                     print()
        
        return 1
def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == 'Q':
            return False
    # Check upper left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1
    # Check upper right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1
    return True

def solve(board, row, n):
    if row == n:
        print_board(board)
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'
            solve(board, row + 1, n)
            board[row][col] = '.'

if __name__ == "__main__":
    n = 4  # You can change n to any positive integer
    board = [['.' for _ in range(n)] for _ in range(n)]
    solve(board, 0, n)