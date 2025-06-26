#!/usr/bin/env python3

def checkmate(board: str) -> None:
    """
    board -> str: String representation of the chessboard, rows separated by newlines.
    invalid board -> returns None
    Success (King is in checked) -> prints "Success"
    Fail (King is not in check) -> prints "Fail"
    """

    # Split the board into rows
    rows = board.strip().split('\n')

    if not rows or not rows[0]:
        print("Invalid board")
        return

    width = len(rows[0])
    height = len(rows)
    if height != width:
        print("Invalid board - not a square")
        return
    for row in rows:
        if len(row) != width:
            print("Invalid board - not a square")
            return

    # get king's position
    king_row, king_col = -1, -1
    king_count = 0
    for r, row in enumerate(rows): #index, item
        for c, cell in enumerate(row):
            if cell == 'K':
                king_row, king_col = r, c
                king_count += 1

    if king_count != 1:
        print("Invalid board - king not found or multiple kings")
        return
    
   
    if check_pawn(rows, king_row, king_col):
        print("Success")
        return
    
    
    if check_bishop(rows, king_row, king_col):
        print("Success")
        return
        
    if check_rook(rows, king_row, king_col):
        print("Success")
        return
    # no need to check queen since it is already checked by bishop and rook
    # queen = bishop + rook
    
    print("Fail")

def check_pawn(board, king_row, king_col):
    # Pawns attack diagonally forward
    rows = len(board)
    cols = len(board[0]) if rows > 0 else 0

    # Pawns can attack from below-left and below-right (assuming they move upward)
    if king_row < rows - 1:
        # left diagonal
        if king_col > 0 and board[king_row + 1][king_col - 1] == 'P':
            return True
        # lower right diagonal
        if king_col < cols - 1 and board[king_row + 1][king_col + 1] == 'P':
            return True

    # can also attack from above-left and above-right (assuming they move downward)
    # if king_row > 0:
    #     # upper left diagonal
    #     if king_col > 0 and board[king_row - 1][king_col - 1] == 'P':
    #         return True
    #     # upper right diagonal
    #     if king_col < cols - 1 and board[king_row - 1][king_col + 1] == 'P':
    #         return True

    return False

def check_bishop(board, king_row, king_col):
    # Check all 4 diagonals, top-left, top-right, bottom-left, bottom-right
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    rows = len(board)
    cols = len(board[0]) if rows > 0 else 0

    for dr, dc in directions:
        r, c = king_row + dr, king_col + dc
        while 0 <= r < rows and 0 <= c < cols:
            if board[r][c] in 'BQ':  # Bishop or Queen
                return True
            elif board[r][c] != '.':  # Any other piece blocks the path
                break
            r, c = r + dr, c + dc
    return False

def check_rook(board, king_row, king_col):
    # Check all 4 directions (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # r, c
    rows = len(board)
    cols = len(board[0]) if rows > 0 else 0

    for dr, dc in directions:
        r, c = king_row + dr, king_col + dc
        while 0 <= r < rows and 0 <= c < cols: # within bounds
            if board[r][c] in 'RQ':  # Rook or Queen
                return True
            elif board[r][c] != '.':  # Any other piece blocks the path
                break
            r, c = r + dr, c + dc
    return False
