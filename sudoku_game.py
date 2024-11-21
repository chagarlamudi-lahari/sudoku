import random

def print_grid(grid):
    """Prints the Sudoku grid."""
    for row in grid:
        print(" ".join(str(cell) if cell != 0 else '.' for cell in row))

def is_valid_move(grid, row, col, num):
    """Checks if placing a number in a specific position is valid."""
    # Check row
    if num in grid[row]:
        return False

    # Check column
    if num in [grid[r][col] for r in range(9)]:
        return False

    # Check 3x3 sub-grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if grid[r][c] == num:
                return False

    return True

def solve_sudoku(grid):
    """Solves the Sudoku puzzle using backtracking."""
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid_move(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

def generate_puzzle():
    """Generates a Sudoku puzzle with random empty cells."""
    grid = [[0] * 9 for _ in range(9)]
    for _ in range(12):  # Add 12 random numbers
        row, col, num = random.randint(0, 8), random.randint(0, 8), random.randint(1, 9)
        while not is_valid_move(grid, row, col, num) or grid[row][col] != 0:
            row, col, num = random.randint(0, 8), random.randint(0, 8), random.randint(1, 9)
        grid[row][col] = num

    # Solve to fill in the rest, then remove some numbers
    solve_sudoku(grid)
    for _ in range(random.randint(40, 50)):
        row, col = random.randint(0, 8), random.randint(0, 8)
        grid[row][col] = 0

    return grid

def play_sudoku():
    """Main function to play the Sudoku game."""
    puzzle = generate_puzzle()
    print("Solve this Sudoku puzzle (enter 0 for empty cells):")
    print_grid(puzzle)

    while True:
        try:
            print("\nEnter your move in the format 'row col num' (or type 'solve' to see the solution):")
            move = input("> ").strip()
            if move.lower() == "solve":
                solve_sudoku(puzzle)
                print("Here's the solution:")
                print_grid(puzzle)
                break
            row, col, num = map(int, move.split())
            if 1 <= row <= 9 and 1 <= col <= 9 and 1 <= num <= 9:
                row, col = row - 1, col - 1
                if is_valid_move(puzzle, row, col, num):
                    puzzle[row][col] = num
                    print("Updated puzzle:")
                    print_grid(puzzle)
                else:
                    print("Invalid move. Try again.")
            else:
                print("Please enter numbers between 1 and 9.")
        except Exception as e:
            print(f"Error: {e}. Try again.")

if __name__ == "__main__":
    play_sudoku()
