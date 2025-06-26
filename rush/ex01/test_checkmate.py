#!/usr/bin/env python3

from checkmate import checkmate

def test_cases():
    # Test Case 1: King in check by a Rook vertically
    board1 = """\
R...
K...
....
....\
"""
    print("Test 1 (Rook vertical check):")
    checkmate(board1)

    # Test Case 2: King in check by a Rook horizontally
    board2 = """\
....
RK..
....
....\
"""
    print("Test 2 (Rook horizontal check):")
    checkmate(board2)

    # Test Case 3: King in check by a Bishop diagonally
    board3 = """\
B...
.K..
....
....\
"""
    print("Test 3 (Bishop diagonal check):")
    checkmate(board3)

    # Test Case 4: King in check by a Queen diagonally
    board4 = """\
Q...
.K..
....
....\
"""
    print("Test 4 (Queen diagonal check):")
    checkmate(board4)

    # Test Case 5: King in check by a Pawn diagonally
    board5 = """\
....
R...
.K..
P...\
"""
    print("Test 5 (Pawn diagonal check):")
    checkmate(board5)

    # Test Case 6: King not in check - pieces blocked
    board6 = """\
R...
PK..
....
....\
"""
    print("Test 6 (Pieces blocked - no check):")
    checkmate(board6)

    # Test Case 7: Invalid board - multiple kings
    board7 = """\
R...
KK..
....
....\
"""
    print("Test 7 (Invalid board - multiple kings):")
    checkmate(board7)

    # Test Case 8: Invalid board - no king
    board8 = """\
R...
....
....
....
"""
    print("Test 8 (Invalid board - no king):")
    checkmate(board8)


    # Test Case 9: Empty board
    board9 = """\
....
....
....
....\
"""
    print("Test 9 (Empty board):")
    checkmate(board9)

if __name__ == "__main__":
    test_cases()
