#!/usr/bin/env python3

import sys
from checkmate import checkmate, validate_board

def process_file(file_path: str) -> str:
    """
    Args:
        file_path (str): Path to the file containing the chess board.
        
    Returns:
        str: "Success" if King is in check, "Error" if board is invalid
    """
    try:
        with open(file_path, 'r') as f:
            board_content = f.read()
            
       
        if not validate_board(board_content):
            # invalid board format
            return "Error"
            
        result = checkmate(board_content)
        
        if result is None:  # Invalid board
            return "Error"
        elif result:
            return "Success"
        else: 
            return "Fail"
    except Exception:
        return "Error"

def main():
   
    if len(sys.argv) < 2:
        print("File path argument is required.")
        return
        
    # Process each file provided as an argument
    for file_path in sys.argv[1:]:
        result = process_file(file_path)
        print(result)

if __name__ == "__main__":
    main()
