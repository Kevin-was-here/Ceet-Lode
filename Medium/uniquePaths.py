'''
There is a robot on an m x n grid. 
The robot is initially located at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths 
that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
'''

m,n =  3,7

def uniquePaths(m,n):
    #Going backwards from the end

    #Create a 2D array of size m x n
    grid = [[0 for i in range(n)] for j in range(m)]

    #Set the last element to 1
    grid[m-1][n-1] = 1

    #Iterate through the grid backwards

    #since we know the next step on the bottom of the grid is = to the next step on the right
    #the bottom of the grid will all be 1
    for i in range(n-1,-1,-1):
        grid[m-1][i] = 1
    
    #similarly the right side of the grid will all be 1
    for i in range(m-1,-1,-1):
        grid[i][n-1] = 1
    
    #The rest of the grid will be the sum of the right and bottom of the grid
    for i in range(m-2, -1, -1):
        for j in range(n-2,-1,-1):
            grid[i][j] = grid[i+1][j] + grid[i][j+1]
            #grid[i][j] = valu below + value right

    return grid[0][0]

print(uniquePaths(m,n))