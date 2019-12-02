number_grid = [
[1,2,3],
[4,5,6],
[7,8,9],
[0]]


#accessing items from the grid
#matrix[row][col]

row=len(number_grid)
col = len(number_grid[0])

for row in number_grid :
    for col in row :
        print(col)


## Dynamic Array Allocation
rows = 3
cols = 2



a =[[0] * cols] * rows
k = 0

#number of rows
for i in range(len(a)):
    #number of columns
    for j in range(len(a[0])):
        k +=1
        a[i][j]=k


print(a)

b = [[1]*3]*2

print(b)

c = [['a']*4]*5

print(c)

## counting the number of walls  in a matrix
## provided 1 is a wall and 0 is a free space
## given the matrix =[[1,0,0,1],[0,1,1,0],[1,1,0,0]]


def find_walls(matrix):
    num_walls =0
    #num of rows
    for i in range(len(matrix)):
        #num of cols
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                num_walls +=1
    return num_walls

matrix = [[1,0,0,1],[0,1,1,0],[1,1,0,0]] 

print(find_walls(matrix))




rows = 3
cols = 2


a =[([0]* cols) for row in range(rows)]

b = [[0]*cols]*rows
print(a)
print(b)


x = [8]*3


print(x)


if 4 in x :
    print('fff')
else :
    print('....')