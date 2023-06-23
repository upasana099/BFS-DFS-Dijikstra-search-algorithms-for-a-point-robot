# BFS-DFS-Dijikstra-search-algorithms-for-a-point-robot
The point robot starts in the Northwest corner of the world and travels to the Southeast corner. Stationary obstacles are placed randomly according to a preset density, which the robot must avoid.

#Helper Functions:**


def obstacle_field
The function obstacle_field generates a 2D matrix with dimensions of 128x128 and sets all its elements to 1. It then calculates the number of shapes required to be placed on the matrix based on the coverage (coverage_list) input.
It then uses the shape_1, shape_2, shape_3 and shape_4 functions to place different shapes of size 4 on the matrix. The shapes are placed at random x and y coordinates and the number of shapes placed is equal to the number of shapes required.Finally, the function returns the 2D matrix with the placed shapes.

def check_valid 
The function checks if a given cell in a 2D array "my_field" is valid to visit or not. It returns False if the cell is out of bounds (row or col is less than 0 or greater than 127), if the cell value is 0, or if the cell is already visited (as marked in the "visited" 2D array). Otherwise, it returns True, indicating that the cell is valid to visit.

def corner
The function is checking the neighbors of a cell in a 2D array (my_field) to see if it's a valid 0-value cell that hasn't been visited yet. The function takes in the 2D array, a list of visited cells (visited), and the x and y coordinates of the current cell being evaluated. The function uses these inputs to determine if the neighbors of the current cell are valid 0-value cells that haven't been visited yet. If a neighbor meets these conditions, it is added to the my_list and returned at the end of the function.

Search Traversal Functions: 
def BFS
Breadth First Search (BFS) algorithm tries to find the shortest path between a starting cell and an end cell in a 2D matrix (my_field). The function takes the 2D matrix, the end point end_pt, and the starting row and column indices row and col as input.
The algorithm starts by initializing the queue q with the starting cell and marking it as visited. It then pops cells from the front of the queue, checks if the end cell is reached, and appends the adjacent cells (that are within the boundaries of the matrix and not already visited) to the end of the queue. The check_valid function checks if a cell is valid, which is defined as being within the boundaries of the matrix and not visited yet. The algorithm continues until the queue is empty, at which point the function returns the number of cells visited (n) and the path.

![BFS](https://github.com/upasana099/BFS-DFS-Dijikstra-search-algorithms-for-a-point-robot/assets/89516193/698bd392-2b15-48fb-93ff-fdb82d41d9b5)

 
**def DFS**
Depth first search (DFS) algorithm in Python. The function takes a 2D matrix my_field, the endpoint end_pt represented as a list [row, col], the starting row row and column col. The function uses a list q as a queue to store cells to be visited, a 2D list visited to store the cells that have already been visited, and two lists Row and Col to store the row and column indices of the adjacents cells.
The function starts by marking the starting cell as visited and adding it to the queue. It then enters a loop, where it pops a cell from the queue, checks if it's the endpoint, and if it's not, it adds its unvisited adjacent cells to the queue. The loop continues until the queue is empty or the endpoint is found. If the endpoint is found, the function returns a tuple of the number of cells visited n and the path to the endpoint represented as a list of coordinates. If the endpoint is not found, the function returns n and an empty list.

![DFS](https://github.com/upasana099/BFS-DFS-Dijikstra-search-algorithms-for-a-point-robot/assets/89516193/bd368bc9-5d71-4d01-afa4-db2737820293)

 
def Dijikstra
Dijkstra algorithm takes a 2D matrix my_field, the endpoint end_point represented as a list [row, col], the starting row row and column col. The function uses a list q as a priority queue to store cells to be visited, a 2D list visited to store the cells that have already been visited, two lists Row and Col to store the row and column indices of the adjacents cells, and a variable cost to store the cost of the path from the starting cell to the current cell.

The function starts by marking the starting cell as visited, adding it to the priority queue with a cost of 0, and setting the path to the endpoint to an empty list. It then enters a loop, where it pops the cell with the lowest cost from the priority queue, checks if it's the endpoint, and if it's not, it adds its unvisited adjacent cells to the priority queue with the updated cost. The loop continues until the priority queue is empty or the endpoint is found. If the endpoint is found, the function returns a tuple of the number of cells visited n and the path to the endpoint represented as a list of coordinates. If the endpoint is not found, the function returns n and None.
![DIJIKSTRA](https://github.com/upasana099/BFS-DFS-Dijikstra-search-algorithms-for-a-point-robot/assets/89516193/82e4b986-fa45-4aac-ab9a-773e3726e610)

 
def random_search
This code implements the random search algorithm. It takes as input a 2-dimensional field represented by a list of lists, an end point represented by a list of two integers [x,y], and the starting row and column as integers.
It first creates a list of visited nodes and a list for the path. It then enters a while loop which runs while the list "my_list" is not empty or the number of iterations exceeds the size of the field squared times 2.
In each iteration, it sets the current node to be the first element of the list "my_list" and adds it to the list of visited nodes and the path. If the current node is equal to the end point, the function returns the number of iterations and the path.
If the current node is not the end point, the function uses the "corner" function to find all the neighboring unvisited nodes and appends one of them to the "my_list". If "my_list" becomes empty, it removes the last node from the path until it is not empty.
If the while loop finishes, the function returns "None" as the path.
NOTE : For Random Search Algorithm, the grid is often not visible to index error and given the high number of iterations, the output is very unpredictable.

Performance Plot:

Plotting 4 pathfinding algorithms (DFS, BFS, Dijkstra, and random search) on a grid with increasing obstacle coverage. The obstacle coverage is calculated as the percentage of the grid that is blocked by obstacles. The algorithms are run for coverage values ranging from 0 to 75 with a step size of 25. The number of iterations each algorithm takes to reach the goal is recorded and plotted against the coverage value.
![Performance plot](https://github.com/upasana099/BFS-DFS-Dijikstra-search-algorithms-for-a-point-robot/assets/89516193/b647e5ec-43fd-4127-85f8-61f4cd983f88)

Planner Path figures:
Three figures depicting the resulting path from each of the planners (DFS, BFS, Dijkstra, and random search) on different Coverage rate of 5%, 10% and 15% respectively.
Blue – BFS
Red – DFS
Green - Dijikstra



 
 

