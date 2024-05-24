import random
import time
import os

def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')  # clear the console
    for row in board:
        print(''.join(row))

def count_neighbors(board, row, col):
    count = 0
    for i in range(max(0, row - 1), min(row + 2, len(board))):
        for j in range(max(0, col - 1), min(col + 2, len(board[0]))):
            if (i, j) != (row, col) and board[i][j] == '█':
                count += 1
    return count

def next_generation(board):
    new_board = [row[:] for row in board]
    for i in range(len(board)):
        for j in range(len(board[0])):
            neighbors = count_neighbors(board, i, j)
            if board[i][j] == '█' and (neighbors < 2 or neighbors > 3):
                new_board[i][j] = ' '
            elif board[i][j] == ' ' and neighbors == 3:
                new_board[i][j] = '█'
    return new_board

def count_living_cells(board):
    return sum(row.count('█') for row in board)

def game_of_life(rows, cols, generations=10):
    board = [['█' if random.random() < 0.5 else ' ' for _ in range(cols)] for _ in range(rows)]
    living_cells_start = count_living_cells(board)
    
    for _ in range(generations):
        print_board(board)
        time.sleep(0.1)
        board = next_generation(board)

    living_cells_end = count_living_cells(board)

    print(f"Living cells at the start: {living_cells_start}")
    print(f"Living cells at the end: {living_cells_end}")

rows, cols = os.get_terminal_size()
print("Rows: ", rows)
print("Columns: ", cols)
generations = int(input('Enter generations: '))
game_of_life(cols, rows, generations)

