#!/usr/bin/env python3

def checkmate(board: str) -> bool:
    """
    Check if the King is in check on the given chessboard.

    Args:
        board (str): String representation of the chessboard, rows separated by newlines.

    Returns:
        bool: True if the King is in check, False otherwise, None if invalid.
    """
   
    rows = board.strip().split('\n')

  
    if not rows or not rows[0]:
        return None

   
    width = len(rows[0])
    for row in rows:
        if len(row) != width:
            return None  # Invalid board, not a square

   
    king_row, king_col = -1, -1
    king_count = 0
    for r, row in enumerate(rows):
        for c, cell in enumerate(row):
            if cell == 'K':
                king_row, king_col = r, c
                king_count += 1

   
    if king_count != 1: # not king or more than one king
        return None
    
    if check_pawn(rows, king_row, king_col):
        return True
        
   
    if check_bishop(rows, king_row, king_col):
        return True
        
    
    if check_rook(rows, king_row, king_col):
        return True
    
    return False

def check_pawn(board, king_row, king_col):
    """Check if any pawn is putting the king in check."""
    # Pawns attack diagonally forward
    # Since all pieces are against the King, we need to check all possible pawn positions
    # that could attack the king diagonally
    rows = len(board)
    cols = len(board[0]) if rows > 0 else 0

    # Check if there's a pawn that can attack the king diagonally
    # Pawns can attack from below-left and below-right (assuming they move upward)
    if king_row < rows - 1:
        # Check lower left diagonal
        if king_col > 0 and board[king_row + 1][king_col - 1] == 'P':
            return True
        # Check lower right diagonal
        if king_col < cols - 1 and board[king_row + 1][king_col + 1] == 'P':
            return True

    # Also check upper diagonals (pawns could be moving downward)
    if king_row > 0:
        # Check upper left diagonal
        if king_col > 0 and board[king_row - 1][king_col - 1] == 'P':
            return True
        # Check upper right diagonal
        if king_col < cols - 1 and board[king_row - 1][king_col + 1] == 'P':
            return True

    return False

def check_bishop(board, king_row, king_col):
    """Check if any bishop or queen is putting the king in check diagonally."""
    # Check all 4 diagonals
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
    """Check if any rook or queen is putting the king in check horizontally or vertically."""
    # Check all 4 directions (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    rows = len(board)
    cols = len(board[0]) if rows > 0 else 0

    for dr, dc in directions:
        r, c = king_row + dr, king_col + dc
        while 0 <= r < rows and 0 <= c < cols:
            if board[r][c] in 'RQ':  # Rook or Queen
                return True
            elif board[r][c] != '.':  # Any other piece blocks the path
                break
            r, c = r + dr, c + dc
    return False

def validate_board(board_str):
    """
    Validate if the board is properly formatted.

    Args:
        board_str (str): String representation of the chessboard.

    Returns:
        bool: True if valid, False otherwise.
    """
  
    if not board_str.strip():
        # empty board
        return False

    # Split into rows
    rows = board_str.strip().split('\n')

    # Check if board has rows
    if len(rows) == 0 or not rows[0]:
        return False

    # Check if board is a valid rectangle
    width = len(rows[0])
    for row in rows:
        if len(row) != width:
            return False

    # Check if there is exactly one King
    king_count = 0
    for row in rows:
        king_count += row.count('K')

    if king_count != 1:
        return False

    return True
