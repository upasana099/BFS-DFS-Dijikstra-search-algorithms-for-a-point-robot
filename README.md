# BFS-DFS-Dijkstra Search Algorithms for a Point Robot

This repository contains Python implementations of Breadth First Search (BFS), Depth First Search (DFS), and Dijkstra search algorithms for a point robot in a 128x128 two-dimensional grid. The goal of the robot is to navigate from the Northwest corner of the grid to the Southeast corner while avoiding randomly placed stationary obstacles.

## Helper Functions

### `obstacle_field`

The `obstacle_field` function generates a 2D matrix with dimensions of 128x128 and randomly places obstacles on the grid based on a specified density. It uses various tetris shape functions (`shape_1`, `shape_2`, `shape_3`, and `shape_4`) to place different shapes of size 4 on the matrix. The function returns the 2D matrix with the placed obstacles.
![Obstacle Field-1](https://github.com/upasana099/BFS-DFS-Dijikstra-search-algorithms-for-a-point-robot/assets/89516193/0663b894-075b-4344-aa32-016ec5418d1a)
Obstacle field with 25% occupancy density

![50%](https://github.com/upasana099/BFS-DFS-Dijikstra-search-algorithms-for-a-point-robot/assets/89516193/5066761e-f817-406f-81bf-4799cad8c753)
Obstacle field with 50% occupancy density

![70%](https://github.com/upasana099/BFS-DFS-Dijikstra-search-algorithms-for-a-point-robot/assets/89516193/c60ab082-e76c-440b-98aa-591fd097a8eb)
Obstacle field with 75% occupancy density

### `check_valid`

The `check_valid` function checks if a given cell in a 2D array `my_field` is valid to visit. It returns `False` if the cell is out of bounds, if the cell value is 0 (indicating an obstacle), or if the cell has already been visited. Otherwise, it returns `True`, indicating that the cell is valid to visit.

### `corner`

The `corner` function checks the neighboring cells of a given cell in a 2D array `my_field` to find valid unvisited cells with a value of 0. It returns a list of the valid neighboring cells.

## Search Traversal Functions

### `BFS`

The `BFS` function implements the Breadth First Search algorithm to find the shortest path between the starting cell and the end cell in a 2D matrix `my_field`. It takes the matrix, the endpoint coordinates (`end_pt`), and the starting row and column indices (`row` and `col`) as input. The algorithm uses a queue to store cells to be visited and a visited 2D list to track the visited cells. It continues until the queue is empty or the endpoint is reached, returning the number of cells visited and the path.
![BFS](https://github.com/upasana099/BFS-DFS-Dijikstra-search-algorithms-for-a-point-robot/assets/89516193/5c83e45e-d15c-4216-a102-cec8bfe9e7e5)

### `DFS`

The `DFS` function implements the Depth First Search algorithm to find a path between the starting cell and the end cell in a 2D matrix `my_field`. It takes the matrix, the endpoint coordinates (`end_pt`), and the starting row and column indices (`row` and `col`) as input. The algorithm uses a stack to store cells to be visited and a visited 2D list to track the visited cells. It continues until the stack is empty or the endpoint is reached, returning the number of cells visited and the path.
![DFS](https://github.com/upasana099/BFS-DFS-Dijikstra-search-algorithms-for-a-point-robot/assets/89516193/9845acdd-4afa-4653-b40a-b4590486d0d9)

### `Dijkstra`

The `Dijkstra` function implements the Dijkstra algorithm to find the shortest path between the starting cell and the end cell in a 2D matrix `my_field`. It takes the matrix, the endpoint coordinates (`end_pt`), and the starting row and column indices (`row` and `col`) as input. The algorithm uses a priority queue to store cells to be visited and a visited 2D list to track the visited cells. It continues until the priority queue is empty or the endpoint is reached, returning the number of cells visited and the path.
![DIJIKSTRA](https://github.com/upasana099/BFS-DFS-Dijikstra-search-algorithms-for-a-point-robot/assets/89516193/10c740a3-5c3f-4268-8184-ca05273262ab)

### `random_search`

The `random_search` function implements a random search algorithm to find a path between the starting cell and the end cell in a 2D matrix. It takes the matrix, the endpoint coordinates (`end_pt`), and the starting row and column indices as input. The algorithm randomly explores neighboring cells until the endpoint is reached or the number of iterations exceeds a threshold. It returns the number of iterations and the path if the endpoint is reached, otherwise, it returns `None`.
NOTE : For Random Search Algorithm, the grid is often not visible to index error and given the high number of iterations, the output is very unpredictable.

## Performance Evaluation

The performance of the search algorithms (BFS, DFS, Dijkstra) can be evaluated using the provided `performance_plot` function. This function generates a performance plot by running the algorithms on a grid with increasing obstacle coverage. The obstacle coverage is calculated as the percentage of the grid that is blocked by obstacles.  The number of iterations each algorithm takes to reach the goal is recorded and plotted against the coverage value.
![Performance plot](https://github.com/upasana099/BFS-DFS-Dijikstra-search-algorithms-for-a-point-robot/assets/89516193/2c66d12e-0ff3-4e77-a661-2dfe2b2f2236)



## Planner Path Figures

The `planner_path_figures` function generates figures depicting the resulting paths from each planner (BFS, DFS, Dijkstra) on grids with different obstacle coverage rates.The obstacle coverage is calculated as the percentage of the grid that is blocked by obstacles.The number of iterations each algorithm takes to reach the goal is recorded and plotted against the coverage value. The paths are color-coded as follows:

- Blue: BFS
- Red: DFS
- Green: Dijkstra

![Planner path at 5%](https://github.com/upasana099/BFS-DFS-Dijikstra-search-algorithms-for-a-point-robot/assets/89516193/a7c786e9-4fa9-48c6-a4c0-8fbb57cfc930)

Planner path at 5% occupancy grid

![Planner path at 10%](https://github.com/upasana099/BFS-DFS-Dijikstra-search-algorithms-for-a-point-robot/assets/89516193/6f9fb31e-d22b-48c3-93fa-812802089833)

Planner path at 10% occupancy grid

![Planner path at 15%](https://github.com/upasana099/BFS-DFS-Dijikstra-search-algorithms-for-a-point-robot/assets/89516193/5c308c16-6c6f-4de3-a4a7-cf5f57d3a4ca)

Planner path at 10% occupancy grid

These figures provide visual representations of the paths found by each algorithm under varying obstacle conditions.

Please refer to the code and function documentation for more details on the implementation and usage of the search algorithms.
