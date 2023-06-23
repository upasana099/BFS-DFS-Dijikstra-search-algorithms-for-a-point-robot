import numpy as np
import matplotlib.pyplot as plt
from  random import randint
from collections import deque as queue
from math import dist
from random import randint, choice

def shape_1(my_field,x_cord,y_cord):
 my_field[x_cord,y_cord]=0
 my_field[x_cord:x_cord+3,y_cord+1]=0
 


def shape_2(my_field,x_cord,y_cord):
  my_field[x_cord:x_cord+2,y_cord]=0
  my_field[x_cord:x_cord+3,y_cord+1]=0
  

def shape_3(my_field,x_cord,y_cord):
  my_field[x_cord:x_cord+2,y_cord]=0
  my_field[x_cord+1:x_cord+3,y_cord+1]=0
 
def shape_4(my_field,x_cord,y_cord):
  my_field[x_cord+1,y_cord]=0
  my_field[x_cord:x_cord+3,y_cord+1]=0
  

def obstacle_field(coverage_list):  
  my_field = np.ones((128,128))
  #coverage_list = int(input('Enter Coverage :'))
  num_of_shapes = ((128*128)*(coverage_list/100))/4
  for i in range(int(num_of_shapes)):
    x_cord = randint(1,126)
    y_cord = randint(1,126)
    if (x_cord > 128):
        x_cord = 126
    if (y_cord > 128):
        y_cord = 126      
    shape_type = randint(1,4)
    if shape_type == 1:
      shape_1(my_field,x_cord,y_cord)
    elif shape_type == 2:
      shape_2(my_field,x_cord,y_cord)
    elif shape_type == 3:
      shape_3(my_field,x_cord,y_cord)
    elif shape_type == 4:
      shape_4(my_field,x_cord,y_cord)
  
  count = np.sum(my_field)
  print(f'Number of shapes utilized = {count}')
  return my_field



def check_valid(my_field, visited, row, col):
  
    # If store lies out of bounds
    if (row < 0 or col < 0 or row > 127 or col > 127):
        return False

    if (my_field[row][col] == 0):
      return False

    # If store is already visited
    if (visited[row][col]):
        return False
 
    # Otherwise
    return True
 


def BFS(my_field, end_pt , row, col):
    Row = [ -1, 0, 1, 0]
    Col = [ 0, 1, 0, -1] 
    visited = [[ False for i in range(len(my_field))] for i in range(len(my_field))]


    q = []
    path=[]
    
    q.append(( row, col,path))
    visited[row][col] = True
 
    # Iterate while the queue
    # is not empty
    n = 0
    while (len(q) > 0):
        n += 1
        store = q.pop(0)
        
        x = store[0]
        y = store[1]
        path = store[2]

        if end_pt == [x,y]:
            return n,path
 
        # Go to the adjacent cell
        for i in range(4):
            adjacent_x = x + Row[i]
            adjacent_y = y + Col[i]
            if (check_valid(my_field ,visited, adjacent_x, adjacent_y)):
                q.append((adjacent_x, adjacent_y,path + [[x,y]]))
                visited[adjacent_x][adjacent_y] = True
        

    return n, path





def DFS(my_field, end_pt , row, col):
    u = 0
    Row = [ -1, 0, 1, 0]
    Col = [ 0, 1, 0, -1] 
    visited = [[ False for i in range(len(my_field))] for i in range(len(my_field))]
   
    q = []
    path=[]
    
    q.append(( row, col,path))
    visited[row][col] = True
 

    u = 0
    while (len(q) > 0):
        u += 1
        store = q.pop()
        
        x = store[0]
        y = store[1]
        
        path = store[2]

        if end_pt == [x,y]:
            return n,path

        for i in range(4):
            adjacent_x = x + Row[i]
            adjacent_y = y + Col[i]
            if (check_valid(my_field ,visited, adjacent_x, adjacent_y)):
                q.append((adjacent_x, adjacent_y,path + [[x,y]]))
                visited[adjacent_x][adjacent_y] = True
        

    return n, path

def Dijikstra(my_field,end_point,row, col):
    n = 0
    Row = [ -1, 0, 1, 0,1,1,-1,-1]
    Col = [ 0, 1, 0, -1,1,-1,1,-1]
    visited = [[ False for i in range(len(my_field))] for i in range(len((my_field)))]                                                         
   
    q = []
    path=[]
    cost=0

    q.append(( row, col,path,cost))
    visited[row][col] = True
 
    while (len(q) > 0):
        n+=1
        store = q.pop(0)
        x = store[0]
        y = store[1]
        path = store[2]
        cost = store[3]
         
        #q.pop()
        if end_point == [x,y]:
            return n,path
 
        for i in range(8):
            adjacent_x = x + Row[i] 
            adjacent_y = y + Col[i]
            current = [x,y]
            if (check_valid(my_field,visited, adjacent_x, adjacent_y)):
                q.append((adjacent_x, adjacent_y,path + [[x,y]],cost + dist(current,[adjacent_x,adjacent_y]) ))
                q = sorted(q, key = lambda x: x[3])
                visited[adjacent_x][adjacent_y] = True
    return n, None


def corner(my_field,visited,x,y):
        my_list = []

        if (x > 0) and (my_field[x-1][y] == 0) and ([x-1,y] not in visited):
            my_list.append([x-1, y])
        if (y > 0) and (my_field[x][y-1] == 0) and ([x,y-1] not in visited):
            my_list.append([x, y-1])
        if (x < len(my_list)) and (my_field[x+1][y] == 0) and ([x+1,y] not in visited):
            my_list.append([x+1, y])
        if (y < len(my_list)) and (my_field[x][y+1] == 0) and ([x,y+1] not in visited):
            my_list.append([x, y+1])

        return my_list

def random_search(my_field, end_point, row, col):
        n = 0
        path =  []
        my_list = [row,col]
        visited = [[ False for i in range(len(my_field))] for i in range(len((my_field)))]  
    
        while my_list and n <= len(my_field)*len(my_field)*2:
            n += 1
            current = my_list
            x,y = current
            visited[x][y] = True
            path.append(current)
            if current == end_point:
                return n,path

            my_list = corner(my_field,visited,x,y)
            if my_list:
                my_list = choice(corner(my_field,visited,x,y))
            while not my_list:
                path.pop()
                if not path:
                    break
                x,y = path[-1]
                my_list = corner(my_field,visited,x,y)
                if my_list:
                    my_list = choice(corner(my_field,visited,x,y))
        print('path', path)
        return n,None



#initialisation 
start_point = [0,0]
end_point = [127,127]
my_field = obstacle_field(25)


n,path1 = BFS(my_field,end_point,1,1)
path1 = np.array(path1)
plt.plot(path1[:,1],path1[:,0])
plt.imshow(my_field)
plt.show()

n,path2 = DFS(my_field,end_point,1,1)
path2 = np.array(path2)
plt.plot(path2[:,1],path2[:,0])
plt.imshow(my_field)
plt.show()

n3,path3 = Dijikstra(my_field, end_point, 1, 1)
path3 = np.array(path3)
plt.plot(path3[:,1],path3[:,0])
plt.imshow(my_field)
plt.show()


n4,path4 = random_search(my_field, end_point, 0, 0)
path4 = np.array(path4)
plt.imshow(my_field)
plt.plot(path4[:,1],path4[:,0])
plt.show()




size = 128
coverage_list = [*range(0,76,25)]

row = 0
col = 0
goal = [127,127]

l1 = []
l2 = []
l3 = []
l4 = []

#Plot coverage_list vs iteration

for i in range(len(coverage_list)):
    grid = obstacle_field((i+1)*25)

    i1, path1 = BFS(grid, goal, row, col)
    i2, path2 = DFS(grid, goal, row, col)
    i3, path3 = Dijikstra(grid, goal, row, col)
    i4, path4 = random_search(grid, goal, row, col)

    l1.append(i1)
    l2.append(i2)
    l3.append(i3)
    l4.append(i4)

plt.figure()
plt.plot(coverage_list,l1,label="BFS")
plt.plot(coverage_list,l2,label="DFS")
plt.plot(coverage_list,l3,label="Dijikstra")
plt.plot(coverage_list,l4,label="Random Search")

plt.xlabel("Coverage")
plt.ylabel("Iterations")

# Paths for coverage_list = 5

grid = obstacle_field(5)
i1, path1 = BFS(grid, goal, row, col)
i2, path2 = DFS(grid, goal, row, col)
i3, path3 = Dijikstra(grid, goal, row, col)
i4, path4 = random_search(grid, goal, row, col)

plt.figure()
plt.imshow(grid)
if path1:
    path1 = np.array(path1)
    plt.plot(path1[:,1],path1[:,0],label="Breadth First Search")
else: print("No Path found for BFS")

if path2:
    path2 = np.array(path2)
    plt.plot(path2[:,1],path2[:,0],label="Depth First Search")
else: print("No Path found for DFS")

if path3:
    path3 = np.array(path3)
    plt.plot(path3[:,1],path3[:,0],label="Dijikstra")
else: print("No Path found for Dijikstra")

plt.show()

if path4:
    path4 = np.array(path4)
    plt.plot(path4[:,1],path4[:,0],label="Random Search")
else: print("No Path found for Random Search")

plt.title("Coverage rate ={}".format(5))



# Paths for coverage_list = 10

grid = obstacle_field(10)
i1, path1 = BFS(grid, goal, row, col)
i2, path2 = DFS(grid, goal, row, col)
i3, path3 = Dijikstra(grid, goal, row, col)
i4, path4 = random_search(grid, goal, row, col)

plt.figure()
plt.imshow(grid)
if path1:
    path1 = np.array(path1)
    plt.plot(path1[:,1],path1[:,0],label="DFS")
else: print("No Path found for DFS")

if path2:
    path2 = np.array(path2)
    plt.plot(path2[:,1],path2[:,0],label="BFS")
else: print("No Path found for BFS")

if path3:
    path3 = np.array(path3)
    plt.plot(path3[:,1],path3[:,0],label="Dijikstra")
else: print("No Path found for Dijikstra")

plt.show()

if path4:
    path4 = np.array(path4)
    plt.plot(path4[:,1],path4[:,0],label="Random Search")
else: print("No Path found for Random Search")

plt.title("Coverage rate {}".format(10))



# Paths for coverage_list = 15

grid = obstacle_field(15)
i1, path1 = BFS(grid, goal, row, col)
i2, path2 = DFS(grid, goal, row, col)
i3, path3 = Dijikstra(grid, goal, row, col)
i4, path4 = random_search(grid, goal, row, col)

plt.figure()
plt.imshow(grid)
if path1:
    path1 = np.array(path1)
    plt.plot(path1[:,1],path1[:,0],label="DFS")
else: print("No Path found for DFS")

if path2:
    path2 = np.array(path2)
    plt.plot(path2[:,1],path2[:,0],label="BFS")
else: print("No Path found for BFS")

if path3:
    path3 = np.array(path3)
    plt.plot(path3[:,1],path3[:,0],label="Dijikstra")
else: print("No Path found for Dijikstra")

plt.show()

if path4:
    path4 = np.array(path4)
    plt.plot(path4[:,1],path4[:,0],label="Random Search")
else: print("No Path found for Random Search")

plt.title("Coverage rate {}".format(15))




