import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class SudokuCSP:
    def __init__(self, puzzle):
        self.grid = np.array(puzzle)
        self.size = 9
        self.animation_steps = []
        
    def is_valid(self, row, col, num):
        if num in self.grid[row]:
            return False
        if num in self.grid[:, col]:
            return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if self.grid[i][j] == num:
                    return False
        return True

    def find_empty_cell(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == 0:
                    return i, j
        return None
    
    def solve(self):
        empty_cell = self.find_empty_cell()
        if not empty_cell:
            return True
        
        row, col = empty_cell
        
        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.grid[row][col] = num
                self.animation_steps.append(np.copy(self.grid))
                
                if self.solve():
                    return True
                
                self.grid[row][col] = 0
                self.animation_steps.append(np.copy(self.grid))
        
        return False

    def print_grid(self):
        for row in self.grid:
            print(" ".join(str(num) if num != 0 else '.' for num in row))

def save_grid_image(grid, filename):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xticks(np.arange(0, 10, 1))
    ax.set_yticks(np.arange(0, 10, 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 9)
    ax.grid(True, which='both', color='black', linestyle='-', linewidth=2)
    
    for i in range(9):
        for j in range(9):
            value = grid[i, j]
            if value != 0:
                ax.text(j + 0.5, 8.5 - i, str(value), ha='center', va='center', fontsize=16, color='blue')
    
    plt.savefig(filename, bbox_inches='tight')
    plt.close()

def animate_sudoku_solution(sudoku, num_frames=50):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xticks(np.arange(0, 10, 1))
    ax.set_yticks(np.arange(0, 10, 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 9)
    ax.grid(True, which='both', color='black', linestyle='-', linewidth=2)

    def update(frame):
        ax.clear()
        ax.set_xticks(np.arange(0, 10, 1))
        ax.set_yticks(np.arange(0, 10, 1))
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_xlim(0, 9)
        ax.set_ylim(0, 9)
        ax.grid(True, which='both', color='black', linestyle='-', linewidth=2)

        current_grid = sudoku.animation_steps[frame]
        for i in range(9):
            for j in range(9):
                value = current_grid[i, j]
                if value != 0:
                    ax.text(j + 0.5, 8.5 - i, str(value), ha='center', va='center', fontsize=16, color='blue')

    total_steps = len(sudoku.animation_steps)
    frame_indices = np.linspace(0, total_steps - 1, num=num_frames, dtype=int)  # Pick 50 evenly spaced frames
    ani = animation.FuncAnimation(fig, update, frames=frame_indices, interval=500, repeat=False)

    ani.save('visualization/sudoku_solution.gif', writer='imagemagick', fps=5)  # Save as GIF
    plt.show()

sudoku_puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

sudoku = SudokuCSP(sudoku_puzzle)

if not os.path.exists('visualization'):
    os.makedirs('visualization')

save_grid_image(sudoku.grid, 'visualization/initial_sudoku.png')
sudoku.solve()
save_grid_image(sudoku.grid, 'visualization/solved_sudoku.png')

animate_sudoku_solution(sudoku)
