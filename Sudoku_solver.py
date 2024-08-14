def print_board(board):
    """Function to print the Sudoku board"""
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def find_empty_location(board):
    """Function to find an empty location in the Sudoku board"""
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col
    return None

def is_valid(board, num, pos):
    """Function to check if a number can be placed in a position"""
    # Check the row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check the column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check the 2x2 box
    box_x = pos[1] // 2
    box_y = pos[0] // 2

    for i in range(box_y * 2, box_y * 2 + 2):
        for j in range(box_x * 2, box_x * 2 + 2):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def solve(board):
    """Backtracking algorithm to solve the Sudoku board"""
    empty = find_empty_location(board)
    if not empty:
        return True  # Puzzle solved
    else:
        row, col = empty

    for num in range(1, 5):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0  # Reset if the solution is not valid

    return False

# Example unsolved 4x4 Sudoku puzzle
puzzle = [
    [1, 0, 0, 4],
    [0, 0, 3, 0],
    [0, 2, 0, 0],
    [3, 0, 0, 2]
]

print("Unsolved Sudoku puzzle:")
print_board(puzzle)

if solve(puzzle):
    print("\nSolved Sudoku puzzle:")
    print_board(puzzle)
else:
    print("No solution exists")
