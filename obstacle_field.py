import numpy as np
import matplotlib.pyplot as plt
from  random import randint

def shape_1(grid,x_cord,y_cord):
  grid[x_cord,y_cord]=1
  grid[x_cord:x_cord+3,y_cord+1]=1
 


def shape_2(grid,x_cord,y_cord):
  grid[x_cord:x_cord+2,y_cord]=1
  grid[x_cord:x_cord+3,y_cord+1]=1
  

def shape_3(grid,x_cord,y_cord):
   grid[x_cord:x_cord+2,y_cord]=1
   grid[x_cord+1:x_cord+3,y_cord+1]=1
 
def shape_4(grid,x_cord,y_cord):
    grid[x_cord+1,y_cord]=1
    grid[x_cord:x_cord+3,y_cord+1]=1
  
 
 
#shape[n] = [[0,1],[0,1],[0,1],[0,1]]
#shape[n] = [[0,0],[0,1],[1,1][1,0]]
#shape[n] = [[0,0],[1,1],[1,0],[1,0]]
#shape[n] = [[0,0],[0,1],[1,1],[0,1]]
   
grid = np.zeros((128,128))
coverage = int(input('Enter Coverage :'))
num_of_shapes = ((128*128)*(coverage/100))/4
for i in range(int(num_of_shapes)):
    x_cord = randint(0,126)
    y_cord = randint(0,126)
    shape_type = randint(1,4)
    if shape_type == 1:
        #r,c = shape_1()
        #s1 = np.ones(r,c)
      shape_1(grid,x_cord,y_cord)
    elif shape_type == 2:
      shape_2(grid,x_cord,y_cord)
    elif shape_type == 3:
      shape_3(grid,x_cord,y_cord)
    elif shape_type == 4:
      shape_4(grid,x_cord,y_cord)
  
plt.imshow(grid,cmap='Blues')
plt.show()
count = np.sum(grid)
print(f'Number of shapes utilized = {count}')