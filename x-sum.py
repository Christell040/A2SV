def calc_max(board_row, board_col, board):
    max_sum = 0
    for r in range(0, board_row):
        for c in range(0, board_col):
            current_sum = board[r][c]
            current_row, current_col = r, c
            
            # Upper left
            while current_row > 0 and current_col > 0:
                current_row -= 1
                current_col -= 1
                current_sum += board[current_row][current_col]
            
            current_row, current_col = r, c
            # Upper right
            while current_row > 0 and current_col < board_col - 1:
                current_row -= 1
                current_col += 1
                current_sum += board[current_row][current_col]
            
            current_row, current_col = r, c
            # Lower left
            while current_row < board_row - 1 and current_col > 0:
                current_row += 1
                current_col -= 1
                current_sum += board[current_row][current_col]
            
            current_row, current_col = r, c
            # Lower right
            while current_row < board_row - 1 and current_col < board_col - 1:
                current_row += 1
                current_col += 1
                current_sum += board[current_row][current_col]
            
            max_sum = max(max_sum, current_sum)
    
    return max_sum


N = int(input())

for _ in range(0, N):
    dimensions = list(map(int, input().split()))
    board_row = dimensions[0]
    board_col = dimensions[1]
    board = [list(map(int, input().split())) for _ in range(0, board_row)]
    
    max_sum = calc_max(board_row, board_col, board)
            
    print(max_sum)
