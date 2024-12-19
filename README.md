# Max Flow and CSP Projects

This repository contains two distinct projects:

1. **Max Flow Problem - Dinic's Algorithm**
   - **Description**: Implementation of the Max Flow problem using Dinic's Algorithm to solve a water distribution network problem.
   - **Key Features**:
     - Solves a real-world problem using a graph-based algorithm.
     - Includes visualizations of initial and solved networks.
     - Unit tests for algorithm validation.
   - **Folder**: `/max-flow-algorithms`
     - `dinics_algorithm.py` - Implementation of Dinic's Algorithm.
     - `test_cases_water_distribution.py` - Unit tests to validate the algorithm.
     - `visualization/` - Folder containing images of the initial and final water distribution networks.
     - `visualize_water_distribution.py` - Script for visualizing the water distribution network.

2. **CSP - Sudoku Problem**
   - **Description**: Solves a Sudoku puzzle using the Constraint Satisfaction Problem (CSP) approach with backtracking and forward checking.
   - **Key Features**:
     - Solves Sudoku puzzles interactively.
     - Visualizes the solving process with animations.
     - Saves initial and final puzzle images, and an animation of the solving process.
   - **Folder**: `/csp`
     - `sudoku.py` - The main script to solve Sudoku using CSP.
     - `visualization/` - Folder containing the initial puzzle, solved puzzle image, and the animation GIF of the solving process.

## Requirements
- Python 3.6+
- To install all the required libraries, you can use the `requirements.txt` file.


## How to Run

### Max Flow Problem
1. Navigate to the `max-flow-algorithms` folder:
   ```bash
   cd max-flow-algorithms

2. To run the visualization:

```
python visualize_water_distribution.py
```

3. To run the unit tests:

```
python -m unittest test_cases_water_distribution.py
```

### CSP - Sudoku Problem

1. Navigate to the csp folder:

```
cd csp
```

2. To solve the Sudoku and visualize the process, run the `sudoku.py` script:

```
python sudoku.py
```

3. The script will generate the `visualization/` folder containing:

 - `initial_sudoku.png` - The initial Sudoku puzzle.
 - `solved_sudoku.png` - The solved Sudoku puzzle.
 - `sudoku_solution.gif` - The animation of the solving process.